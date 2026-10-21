(function(){
  /* brand icons: <span data-icon="python"></span> */
  var I=window.ICONS||{};
  function lum(h){var n=parseInt(h.slice(1),16);return (0.299*(n>>16&255)+0.587*(n>>8&255)+0.114*(n&255))/255;}
  document.querySelectorAll('[data-icon]').forEach(function(el){
    var k=I[el.getAttribute('data-icon')]; if(!k) return;
    el.innerHTML='<svg viewBox="0 0 24 24" role="img" aria-label="'+k.t+'"><path fill="'+(lum(k.h)<0.3?'#ffffff':k.h)+'" d="'+k.p+'"/></svg>';
  });

  /* copy email */
  var copy=document.getElementById('copy'),toast=document.getElementById('toast'),mail=document.getElementById('mail');
  if(copy&&mail){copy.addEventListener('click',function(){
    function select(){var r=document.createRange();r.selectNodeContents(mail);var s=getSelection();s.removeAllRanges();s.addRange(r);toast.textContent='Email selected. Press Ctrl+C or ⌘C to copy it.';}
    try{navigator.clipboard.writeText(mail.textContent).then(function(){toast.textContent='Email copied.';},select);}catch(e){select();}
  });}

})();
