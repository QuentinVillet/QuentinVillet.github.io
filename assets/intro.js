// Home intro: a MacBook under a spotlight. The light comes on, the lid opens,
// the screen boots and loads the site, and a click flies the camera into the screen.
// MacBook model: pmndrs/examples (MIT licence), see assets/vendor/MACBOOK-MODEL-LICENSE.txt
import * as THREE from './vendor/three.module.min.js';
import { GLTFLoader } from './vendor/GLTFLoader.js';
import { RoomEnvironment } from './vendor/RoomEnvironment.js';

const intro = document.getElementById('intro');
if (intro) run();

function run() {
  let seen = false;
  try { seen = sessionStorage.getItem('qv-intro') === '1'; } catch (e) {}
  if (seen || location.hash) { intro.hidden = true; return; }
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  window.scrollTo({ top: 0, behavior: 'instant' });
  document.documentElement.style.overflow = 'hidden';

  const canvas = intro.querySelector('canvas');
  const fade = document.getElementById('fade');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ canvas, antialias: true }); } catch (e) { finish(); return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x050506);
  const pmrem = new THREE.PMREMGenerator(renderer);
  const envTex = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environment = envTex;

  const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 200);
  const LOOK = new THREE.Vector3(0, 1.9, 2.4);
  const START = new THREE.Vector3(0, 14, 33);
  const REST = new THREE.Vector3(0, 10.5, 25.5);

  // floor: concrete, lit by one spotlight
  const floorTex = new THREE.CanvasTexture(concrete(1024));
  floorTex.wrapS = floorTex.wrapT = THREE.MirroredRepeatWrapping;
  floorTex.repeat.set(4, 4);
  floorTex.colorSpace = THREE.SRGBColorSpace;
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(120, 120),
    new THREE.MeshStandardMaterial({ map: floorTex, color: 0x8d8d90, roughness: 0.95, metalness: 0, envMapIntensity: 0.05 }));
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -0.21;
  floor.receiveShadow = true;
  scene.add(floor);

  const spot = new THREE.SpotLight(0xfff6ee, 0, 0, 0.34, 1, 1.6);
  const amb = new THREE.HemisphereLight(0x9090a0, 0x000000, 0);
  scene.add(amb);
  spot.position.set(0, 26, 6);
  spot.target.position.set(0, 0, 2.6);
  spot.castShadow = true;
  spot.shadow.mapSize.set(2048, 2048);
  spot.shadow.radius = 8;
  spot.shadow.bias = -0.0005;
  scene.add(spot, spot.target);
  const SPOT_MAX = 2600;

  // screen: a canvas we draw the boot screen and the site onto
  const SW = 1440, SH = 900;
  const scr = document.createElement('canvas'); scr.width = SW; scr.height = SH;
  const g = scr.getContext('2d');
  const scrTex = new THREE.CanvasTexture(scr);
  scrTex.colorSpace = THREE.SRGBColorSpace;
  scrTex.flipY = false;
  scrTex.anisotropy = renderer.capabilities.getMaxAnisotropy();
  const siteImg = new Image();
  let siteReady = false;
  siteImg.onload = () => { siteReady = true; };
  siteImg.src = new URL('screen-site.jpg', import.meta.url).href;

  const screenLight = new THREE.PointLight(0x9a9aff, 0, 9, 2);
  scene.add(screenLight);

  let hinge = null, screenMesh = null, mac = null;
  const CLOSED = 1.575, OPEN = -0.36;
  let lid = CLOSED, t0 = performance.now(), state = 'dark', bootT = 0, bootStart = 0, diving = null, alive = true;
  const pointer = { x: 0, y: 0 }, drift = { x: 0, y: 0 };

  new GLTFLoader().load(new URL('macbook.glb', import.meta.url).href, (gltf) => {
    mac = gltf.scene;
    mac.traverse((o) => {
      if (o.isMesh) {
        o.castShadow = true; o.receiveShadow = true;
        const m = o.material;
        if (m.name === 'aluminium') { m.color.set(0x8a8c91); m.metalness = 1; m.roughness = 0.38; m.envMapIntensity = 1.1; }
        if (m.name === 'matte.001') { m.color.set(0x0a0a0b); m.roughness = 0.5; }
        if (m.name === 'keys') { m.color.set(0x111113); m.roughness = 0.55; }
        if (m.name === 'trackpad') { m.color.set(0x76787d); m.metalness = 0.8; m.roughness = 0.3; }
        if (m.name === 'touchbar') { m.color.set(0x050505); }
        if (m.name === 'screen.001') {
          o.material = new THREE.MeshBasicMaterial({ map: scrTex, toneMapped: false });
          screenMesh = o;
        }
      }
    });
    hinge = mac.getObjectByName('screenflip');
    hinge.rotation.x = CLOSED;
    scene.add(mac);
    t0 = performance.now();
    state = reduce ? 'idle' : 'light';
    if (reduce) { lid = OPEN; spot.intensity = SPOT_MAX; amb.intensity = 0.35; bootT = 99; intro.classList.add('ready'); }
  }, undefined, () => finish());

  function size() {
    const w = intro.clientWidth, h = intro.clientHeight, a = w / h;
    renderer.setSize(w, h, false);
    camera.aspect = a;
    camera.fov = a < 1 ? 30 + (1 - a) * 38 : 30;
    camera.updateProjectionMatrix();
  }
  size();
  addEventListener('resize', size);
  intro.addEventListener('pointermove', (e) => {
    pointer.x = e.clientX / innerWidth - 0.5;
    pointer.y = e.clientY / innerHeight - 0.5;
  });

  const ease = (p) => (p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2);
  const easeOut = (p) => 1 - Math.pow(1 - p, 3);
  const spring = (p) => 1 - Math.exp(-6 * p) * Math.cos(9 * p);

  function drawScreen(now) {
    // 0-0.5s black, 0.5-1.6s logo and progress bar, then the site fades in and scrolls slowly
    g.fillStyle = '#000'; g.fillRect(0, 0, SW, SH);
    if (bootT < 0.5) return;
    if (bootT < 2.1) {
      const a = Math.min(1, (bootT - 0.5) / 0.4);
      g.globalAlpha = a;
      const grd = g.createRadialGradient(SW / 2, SH * 1.1, 10, SW / 2, SH * 1.1, SH);
      grd.addColorStop(0, '#3b3bb0'); grd.addColorStop(1, '#000');
      g.fillStyle = grd; g.fillRect(0, 0, SW, SH);
      g.fillStyle = '#fff'; g.font = '300 120px Outfit, Inter, system-ui, sans-serif'; g.textAlign = 'center'; g.textBaseline = 'middle';
      g.fillText('QV', SW / 2, SH / 2 - 40);
      g.fillStyle = 'rgba(255,255,255,.18)'; round(g, SW / 2 - 140, SH / 2 + 90, 280, 6, 3); g.fill();
      g.fillStyle = '#fff'; round(g, SW / 2 - 140, SH / 2 + 90, 280 * Math.min(1, (bootT - 0.6) / 1.3), 6, 3); g.fill();
      g.globalAlpha = 1;
      return;
    }
    if (!siteReady) return;
    const a = Math.min(1, (bootT - 2.1) / 0.6);
    const maxY = siteImg.height - SH;
    const cyc = reduce || diving ? 0 : ((bootT - 3.2) % 18 + 18) % 18;
    const k = bootT < 3.2 ? 0 : cyc < 3 ? 0 : cyc < 8 ? ease((cyc - 3) / 5) : cyc < 11 ? 1 : cyc < 15 ? 1 - ease((cyc - 11) / 4) : 0;
    g.globalAlpha = a;
    g.drawImage(siteImg, 0, k * maxY * 0.7, SW, SH, 0, 0, SW, SH);
    g.globalAlpha = 1;
  }

  let last = performance.now();
  function frame(now) {
    if (!alive) return;
    const dt = Math.min(0.05, (now - last) / 1000); last = now;
    const t = (now - t0) / 1000;
    if (mac) {
      if (state === 'light') {
        spot.intensity = SPOT_MAX * easeOut(Math.min(1, t / 1.2));
        amb.intensity = 0.35 * easeOut(Math.min(1, t / 1.2));
        if (t > 0.9) { state = 'open'; t0 = now; }
      } else if (state === 'open') {
        const p = Math.min(1, t / 2.2);
        lid = CLOSED + (OPEN - CLOSED) * spring(p);
        if (t > 1.1 && !bootStart) bootStart = now;
        if (bootStart) bootT = (now - bootStart) / 1000;
        if (p >= 1) { state = 'idle'; intro.classList.add('ready'); }
      } else if (state === 'idle') {
        if (!bootStart) bootStart = now - bootT * 1000;
        bootT = (now - bootStart) / 1000;
      }
      hinge.rotation.x = lid;
      const on = Math.min(1, Math.max(0, (bootT - 0.4) / 0.6));
      screenLight.intensity = on * 5;
      screenLight.position.set(0, 3.2, 1.6);
      drawScreen(now);
      scrTex.needsUpdate = true;
    }

    if (diving) {
      const p = Math.min(1, (now - diving.t) / diving.ms), e = ease(p);
      camera.position.lerpVectors(diving.from, diving.to, e);
      camera.lookAt(new THREE.Vector3().lerpVectors(diving.lookFrom, diving.lookTo, e));
      if (p > 0.8 && !diving.faded) { diving.faded = true; fade.classList.add('on'); }
      if (p >= 1) { finish(); return; }
    } else {
      // dolly in while the laptop opens, then drift with the pointer
      const intoRest = state === 'idle' ? 1 : state === 'open' ? ease(Math.min(1, (now - t0) / 2200)) : 0;
      drift.x += (pointer.x * 3 - drift.x) * 0.04;
      drift.y += (-pointer.y * 1.4 - drift.y) * 0.04;
      camera.position.lerpVectors(START, REST, intoRest);
      camera.position.x += drift.x * intoRest;
      camera.position.y += drift.y * intoRest;
      camera.lookAt(LOOK);
    }
    renderer.render(scene, camera);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  function dive() {
    if (diving || !screenMesh) return;
    intro.classList.add('diving');
    if (reduce) { fade.classList.add('on'); setTimeout(finish, 250); return; }
    lid = OPEN; hinge.rotation.x = OPEN; state = 'diving'; bootT = Math.max(bootT, 3); mac.updateMatrixWorld(true);
    screenMesh.geometry.computeBoundingBox();
    const box = screenMesh.geometry.boundingBox.clone().applyMatrix4(screenMesh.matrixWorld);
    const centre = box.getCenter(new THREE.Vector3());
    const normal = new THREE.Vector3(0, Math.sin(-OPEN), Math.cos(-OPEN)).normalize();
    const h = box.max.y - box.min.y;
    const dist = (h / 2) / Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)) * 1.02;
    diving = { t: performance.now(), ms: 1600, from: camera.position.clone(), to: centre.clone().add(normal.multiplyScalar(dist)),
      lookFrom: LOOK.clone(), lookTo: centre, faded: false };
  }
  canvas.addEventListener('click', dive);
  canvas.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); dive(); } });
  document.getElementById('skip').addEventListener('click', finish);

  function finish() {
    alive = false;
    try { sessionStorage.setItem('qv-intro', '1'); } catch (e) {}
    intro.hidden = true;
    document.documentElement.style.overflow = '';
    window.scrollTo({ top: 0, behavior: 'instant' });
    requestAnimationFrame(() => { window.scrollTo({ top: 0, behavior: 'instant' }); if (fade) fade.classList.remove('on'); });
    if (renderer) renderer.dispose();
  }
}

function round(g, x, y, w, h, r) { g.beginPath(); g.roundRect ? g.roundRect(x, y, Math.max(0, w), h, r) : g.rect(x, y, w, h); }
function concrete(n) {
  const c = document.createElement('canvas'); c.width = c.height = n;
  const g = c.getContext('2d'), img = g.createImageData(n, n);
  for (let i = 0; i < n * n; i++) { const v = 148 + (Math.random() - 0.5) * 22; img.data[i * 4] = img.data[i * 4 + 1] = img.data[i * 4 + 2] = v; img.data[i * 4 + 3] = 255; }
  g.putImageData(img, 0, 0);
  for (let i = 0; i < 160; i++) {
    const x = Math.random() * n, y = Math.random() * n, r = 30 + Math.random() * 180;
    const grd = g.createRadialGradient(x, y, 0, x, y, r), d = Math.random() < 0.55 ? '0,0,0' : '255,255,255';
    grd.addColorStop(0, `rgba(${d},${0.04 + Math.random() * 0.05})`); grd.addColorStop(1, `rgba(${d},0)`);
    g.fillStyle = grd; g.fillRect(x - r, y - r, r * 2, r * 2);
  }
  return c;
}
