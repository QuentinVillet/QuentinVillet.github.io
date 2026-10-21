"""Builds Quentin's portfolio. Run: python3 build.py"""
from pathlib import Path


ROOT = Path(__file__).parent
CV = "cv/Quentin_Villet_CV.pdf"
EMAIL = "quentinxvillet@gmail.com"
GH = "https://github.com/QuentinVillet"
LI = "https://www.linkedin.com/in/quentinvillet"

GH_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.52-1.33-1.28-1.69-1.28-1.69-1.05-.72.08-.7.08-.7 1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.56-.29-5.25-1.28-5.25-5.69 0-1.26.45-2.29 1.19-3.1-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.84 1.19 3.1 0 4.42-2.7 5.39-5.27 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5Z"/></svg>'
LI_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.95v5.66H9.34V9h3.42v1.56h.05a3.75 3.75 0 0 1 3.37-1.85c3.6 0 4.27 2.37 4.27 5.46v6.28ZM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13ZM7.12 20.45H3.56V9h3.56v11.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0Z"/></svg>'
DL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>'
ARROW = '<svg class="arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>'
BEAM = '<div class="lines"></div><div class="beam" aria-hidden="true"><i class="b1"></i><i class="soft"><b class="cone"></b><b class="rays"></b></i><i class="soft2"><b class="core"></b></i></div>'

NAV = [("index.html", "Home", "opt"), ("experience.html", "Experience", ""), ("projects.html", "Projects", ""), ("studies.html", "Studies & skills", "opt")]


def page(path, title, desc, body, current, home=False):
    up = "../" * path.count("/")
    links = "".join(f'<li class="{c}"><a href="{up}{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>' for h, t, c in NAV)
    intro = ""
    if home:
        intro = """<div class="intro" id="intro">
  <canvas tabindex="0" aria-label="A laptop opening and loading Quentin Villet's website. Click it to enter."></canvas>
  <div class="intro-hint"><span>Click the screen to come in</span><button id="skip" type="button">Skip</button></div>
</div>
<div class="fade" id="fade"></div>
<script type="module" src="assets/intro.js"></script>"""
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230d0d2b'/%3E%3Ctext x='16' y='21.5' font-family='Arial' font-size='14' fill='%23fff' text-anchor='middle'%3EQV%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500&family=Inter:wght@400;500&display=swap">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
{intro}
<nav class="nav" aria-label="Main"><div class="wrap"><div class="nav-bar">
  <a class="brand" href="{up}index.html"><b>Quentin Villet</b><small>Data science &amp; business</small></a>
  <ul>{links}</ul>
  <a class="btn" href="{up}{CV}" target="_blank" rel="noopener">Download CV</a>
</div></div></nav>
<main>
{body}
</main>
<footer class="foot" id="contact">{BEAM}<div class="wrap foot-in">
  <p class="label">get in touch</p>
  <h2>I'm looking for a summer 2027 internship.</h2>
  <p class="l">Data science, AI or product. If you think I could help your team, send me an email or a message on LinkedIn.</p>
  <div class="mailrow">
    <span class="mail" id="mail">{EMAIL}</span>
    <button class="btn" id="copy" type="button">Copy email</button>
    <a class="btn" href="{LI}" target="_blank" rel="noopener">{LI_SVG} LinkedIn</a>
    <a class="btn" href="{GH}" target="_blank" rel="noopener">{GH_SVG} GitHub</a>
    <a class="btn solid" href="{up}{CV}" target="_blank" rel="noopener">{DL_SVG} Download CV</a>
  </div>
  <p class="toast" id="toast" role="status"></p>
  <div class="foot-bottom"><span>© 2026 Quentin Villet · Paris</span><a href="#">Back to top</a></div>
</div></footer>
<script src="{up}assets/icons.js"></script>
<script src="{up}assets/site.js"></script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


# ------------------------------------------------------------------ data
JOBS = [
    dict(slug="danone", co="Danone", role="Data Scientist intern", dates="Jun – Sep 2026", place="Paris", logos=["danone"],
         kind="Internship · on-site · 4 months", team="Global SiA team",
         short="I built a tool on Databricks that blurs faces, licence plates and names in consumer photos so they can be used under GDPR. Then I used vision models to turn 10,000+ photos into data the insights team could work with."),
    dict(slug="artefact", co="Artefact", role="Data Consultant intern", dates="Mar – Aug 2025", place="Paris", logos=["artefact"],
         kind="Internship · 6 months", team="Data consulting",
         short="I built a Dialogflow chatbot that answers 60 common questions for a large French distribution company, and a BigQuery catalogue of 2,000+ variables."),
    dict(slug="clikalia", co="Clikalia", role="Portfolio Management intern", dates="Jun – Aug 2023", place="Mexico City", logos=["clikalia"],
         kind="Internship · on-site · 3 months", team="Proptech startup",
         short="I moved the credit team's processes into HubSpot and wrote the manuals to train them. I also managed 200+ properties."),
    dict(slug="montagu", co="Montagu", role="Deal team intern", dates="Jun – Jul 2022", place="Paris", logos=["montagu"],
         kind="Internship · 2 months", team="Private equity, Paris office",
         short="Market research, expert calls and due diligence on pharma and tech companies, mostly SaaS."),
]
SCHOOLS = [
    dict(co="CentraleSupélec & ESSEC", role="MSc Data Science & Business Analytics", dates="2025 – 2027", place="Paris", logos=["centralesupelec", "essec"],
         short="A joint degree between an engineering school and a business school.",
         classes=["Machine Learning", "Statistics", "Optimization", "Linear Algebra", "Databases", "C++", "Econometrics"]),
    dict(co="Le Wagon", role="Data Science & AI bootcamp", dates="Oct – Dec 2024", place="London", logos=["lewagon"],
         short="Ten weeks of full-time coding. Our final project was HarmonIQ.",
         classes=["Python", "Machine learning", "Deep learning", "Docker", "GCP"]),
    dict(co="Bocconi University", role="BSc Economics & International Management", dates="2021 – 2024", place="Milan", logos=["bocconi"],
         short="My thesis looked at what helps Bocconi graduates' startups succeed.",
         classes=["Statistics", "Data analysis", "Corporate finance", "Macroeconomics", "Microeconomics", "Stata"]),
]
PROJECTS = [
    dict(id="leasely", title="Leasely", ctx="Apple × MWM Build Challenge, Oct 2026", img="leasely-tabs.jpg", light=True,
         d="An iPhone app that helps French landlords rent out a flat without an agency: scan the energy certificate, check what the law allows, generate the lease and sign it. We built it in two days, as a team of four.",
         chips=["SwiftUI", "Apple Foundation Models", "Vision", "PDFKit"]),
    dict(id="fuelx", title="FuelX", ctx="Side project, 2026", img="fuelx-screens.jpg",
         url="https://github.com/QuentinVillet/fuelx-meal-analyzer",
         d="Take a photo of your meal, say how hard you trained, and get a score out of 10 with one thing to change. It runs on a free, local vision model.",
         chips=["Python", "LLaVA", "Streamlit", "SQLite", "Docker"]),
    dict(id="harmoniq", title="HarmonIQ", ctx="Le Wagon final project, 2024", img="harmoniq-clusters.jpg",
         url="https://github.com/QuentinVillet/HarmonIQ",
         d="Playlists made from the songs you already like. We grouped over a million Spotify tracks into 100 clusters and deployed it with FastAPI and Docker on GCP.",
         chips=["PCA", "K-means", "FastAPI", "GCP"]),
    dict(id="bias", title="Political bias in the news", ctx="Machine learning class project", img="bias-matrix.jpg",
         url="https://github.com/ketanpr14-hub/ML-Final-Project",
         d="Placing a news article from left to right using only its words. Most of our model's mistakes were between neighbouring classes.",
         chips=["NLP", "TF-IDF", "SVM", "scikit-learn"]),
    dict(id="kaggle", title="Who will buy?", ctx="Kaggle class competition", img="kaggle-features.jpg",
         url="https://github.com/PaulFrp/kaggle_competition",
         d="Predicting which shoppers will buy during a campaign with XGBoost. 77.8% F1. The number of items in the cart mattered most by far.",
         chips=["XGBoost", "Optuna", "pandas"]),
]
TOOLS = [("python", "Python"), ("pytorch", "PyTorch"), ("huggingface", "Hugging Face"), ("scikitlearn", "scikit-learn"),
         ("pandas", "pandas"), ("databricks", "Databricks"), ("googlebigquery", "BigQuery"), ("googlecloud", "Google Cloud"),
         ("docker", "Docker"), ("fastapi", "FastAPI"), ("swift", "Swift"), ("claude", "Claude Code")]


def logo(item, up="", cls="logo"):
    imgs = "".join(f'<img src="{up}assets/logos/{l}.png" alt="">' for l in item["logos"])
    return f'<span class="{cls}{" pair" if len(item["logos"]) > 1 else ""}" aria-hidden="true">{imgs}</span>'


def xp_row(j, up=""):
    return f"""<li><a href="{up}experience/{j['slug']}.html">{logo(j, up)}
  <div><h3>{j['role']} <span>at {j['co']}</span></h3><p>{j['short']}</p></div>
  <time>{j['dates']}<b>{j['place']}</b></time>{ARROW}</a></li>"""


def school_row(s, up=""):
    cl = "".join(f"<li>{c}</li>" for c in s["classes"])
    return f"""<li><div class="row">{logo(s, up)}
  <div><h3>{s['role']} <span>at {s['co']}</span></h3><p>{s['short']}</p><ul class="classes">{cl}</ul></div>
  <time>{s['dates']}<b>{s['place']}</b></time></div></li>"""


def card(p, up="", wide=False):
    chips = "".join(f"<li>{c}</li>" for c in p["chips"])
    tag, attrs = ("a", f' href="{p["url"]}" target="_blank" rel="noopener"') if p.get("url") else ("div", "")
    foot = f'<span class="gh">{GH_SVG} View the code on GitHub</span>' if p.get("url") else '<span class="gh priv">Private code, built for MWM. Screenshots only.</span>'
    return f"""<{tag} class="card{" wide" if wide else ""}{" static" if not p.get("url") else ""}" id="{p['id']}"{attrs}>
  <div class="pic{" light" if p.get("light") else ""}"><img src="{up}assets/{p['img']}" alt="{p['title']}" loading="lazy"></div>
  <div class="txt"><span class="ctx">{p['ctx']}</span><h3>{p['title']}</h3><p class="d">{p['d']}</p><ul class="chips">{chips}</ul>
  {foot}</div>
</{tag}>"""


def tools_grid(items):
    return '<div class="tools">' + "".join(f'<div class="tool"><span data-icon="{s}"></span>{n}</div>' for s, n in items) + "</div>"


# ------------------------------------------------------------------ home
home = f"""
<section class="hero">{BEAM}<div class="wrap" style="width:100%"><div class="hero-copy">
  <h1>Hi, I'm Quentin.</h1>
  <p class="sub">I study data science and business in Paris.</p>
  <p class="lede">I'm in my last year at CentraleSupélec and ESSEC. This is where you can see what I've worked on, what I've built and what I've studied.</p>
  <div class="actions">
    <a class="btn" href="{CV}" target="_blank" rel="noopener">{DL_SVG} Download my CV</a>
    <a class="btn" href="projects.html">See my projects</a>
  </div>
</div></div></section>

<section class="sec"><div class="wrap who">
  <div class="copy">
    <p class="label">who I am</p>
    <h2>From Hong Kong to Paris</h2>
    <p>I was born in Hong Kong and grew up between Hong Kong, Shanghai and Tokyo, then moved back to Hong Kong for high school. After that I studied economics at Bocconi in Milan, and did a data science bootcamp at Le Wagon in London because I wanted to write the code myself.</p>
    <p>This summer I was a data scientist at Danone, working on computer vision. Before that I did data consulting at Artefact, worked at a startup in Mexico City and interned in private equity at Montagu.</p>
    <p>Outside of school I played rugby for Hong Kong's national team. I speak French and English, good Spanish, some Chinese and a little Italian.</p>
    <div class="tagbox"><span><small>Born in</small>Hong Kong</span><span><small>Based in</small>Paris</span><span><small>Graduating</small>June 2027</span><span><small>Looking for</small>Summer 2027 internship</span></div>
  </div>
  <figure class="orb"><img src="assets/quentin.jpg" alt="Quentin smiling with a medal at the Great Wall of China Marathon"><figcaption>At the Great Wall of China Marathon</figcaption></figure>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="head right"><p class="label">what I use</p><h2>Tools I work with</h2></div>
  {tools_grid(TOOLS)}
</div></section>

<section class="sec"><div class="wrap">
  <div class="head"><p class="label">where I've worked</p><h2>Four internships, from Paris to Mexico City</h2></div>
  <ul class="xp">{"".join(xp_row(j) for j in JOBS)}</ul>
</div></section>

<section class="sec alt"><div class="wrap">
  <div class="head right"><p class="label">what I've built</p><h2>Recent projects</h2><p class="intro-p">Click a project to open its code on GitHub.</p></div>
  <div class="grid">{"".join(card(p) for p in PROJECTS[:3])}</div>
  <a class="btn more" href="projects.html">All projects</a>
</div></section>

<section class="sec"><div class="wrap">
  <div class="head"><p class="label">where I've studied</p><h2>Hong Kong, Milan, London, Paris</h2></div>
  <ul class="xp">{"".join(school_row(s) for s in SCHOOLS)}</ul>
  <a class="btn more" href="studies.html">Skills and languages</a>
</div></section>
"""
page("index.html", "Quentin Villet", "Quentin Villet, data science and business student at CentraleSupélec and ESSEC.", home, "index.html", home=True)

# ------------------------------------------------------------------ experience list
exp = f"""
<section class="hero short">{BEAM}<div class="wrap" style="width:100%"><div class="hero-copy">
  <h1>Experience</h1>
  <p class="lede">Private equity, a startup, consulting and a global food company. Click one to read more.</p>
</div></div></section>
<section class="sec"><div class="wrap">
  <ul class="xp">{"".join(xp_row(j) for j in JOBS)}</ul>
</div></section>
"""
page("experience.html", "Experience · Quentin Villet", "Quentin Villet's internships.", exp, "experience.html")


def tags(items):
    out = ""
    for slug, name in items:
        out += f'<li><span data-icon="{slug}"></span>{name}</li>' if slug else f"<li>{name}</li>"
    return f'<ul class="tags">{out}</ul>'


DETAIL = {
"danone": f"""
<p class="lead">I spent the summer in Danone's Global SiA team, working on two computer vision projects. I worked mostly on my own, with a weekly check-in with my manager.</p>
<div class="nums"><div><b>10,000+</b><span>photos turned into data</span></div><div><b>5</b><span>OCR and vision models compared</span></div><div><b>200+</b><span>people I presented to</span></div></div>
<div>
  <h2>Making photos safe to use</h2>
  <p class="t">Consumer photos can show faces, licence plates, names and where they were taken. Under GDPR, the team couldn't use them as they were.</p>
  <ul class="pts" style="margin-top:20px">
    <li>I built a pipeline on Databricks that removes metadata, finds personal information, blurs it, checks the result and writes a risk report.</li>
    <li>I compared EasyOCR, PaddleOCR, docTR and Florence-2 on accuracy and speed before choosing one.</li>
  </ul>
  <div class="flow" style="margin-top:28px"><ol><li><b>Photo in</b><span>from consumers</span></li><li><b>Remove metadata</b><span>GPS, device, date</span></li><li class="hl"><b>Detect</b><span>faces, plates, text</span></li><li><b>Blur</b><span>what was found</span></li><li><b>Check</b><span>scan the result again</span></li><li><b>Report</b><span>risk score as a PDF</span></li></ol></div>
  <p class="cap">A simplified view. The code and photos stay with Danone.</p>
</div>
<div>
  <h2>Turning photos into insight</h2>
  <ul class="pts">
    <li>I used vision-language models on GPU to describe each photo and pull out products, brands, food, drinks and the setting.</li>
    <li>Before building, I sat with the insights team to understand the questions they wanted answered. That changed what I built.</li>
    <li>I presented the results to 200+ people across the global team.</li>
  </ul>
</div>
<div><h2>What I took from it</h2><p class="t">A good model isn't enough. I had to weigh accuracy against GPU access, licences, cost and whether the team would actually use it.</p></div>
<div><h2>Tools</h2>{tags([("databricks","Databricks"),("python","Python"),("pytorch","PyTorch"),("huggingface","Hugging Face"),("opencv","OpenCV"),(None,"YOLO"),(None,"EasyOCR"),(None,"Florence-2")])}</div>
""",
"artefact": f"""
<p class="lead">Artefact is a data and AI consultancy. I worked on client projects for large French companies, mostly on their data.</p>
<div class="nums"><div><b>60</b><span>questions the chatbot answers</span></div><div><b>2,000+</b><span>variables in the catalogue</span></div></div>
<div>
  <h2>What I did</h2>
  <ul class="pts">
    <li><b>Chatbot.</b> I built a chatbot in Python with Dialogflow on GCP. It answers 60 common questions for different types of users at a large French distribution company.</li>
    <li><b>Data catalogue.</b> I built a catalogue in BigQuery that brought 2,000+ variables from different ERP systems under one set of definitions.</li>
    <li><b>Data migration.</b> I wrote SQL to pull and check data for a large migration, and worked directly with the client's teams.</li>
  </ul>
</div>
<div><h2>Tools</h2>{tags([("googlecloud","Google Cloud"),("googlebigquery","BigQuery"),("dialogflow","Dialogflow"),("python","Python"),(None,"SQL"),("looker","Looker Studio")])}</div>
""",
"clikalia": f"""
<p class="lead">Clikalia is a proptech startup. I spent a summer on the portfolio team in Mexico City, between the business and tech sides.</p>
<div class="nums"><div><b>200+</b><span>properties managed</span></div></div>
<div>
  <h2>What I did</h2>
  <ul class="pts">
    <li><b>HubSpot.</b> I moved the credit team's processes into HubSpot and wrote simple manuals to train the team on it.</li>
    <li><b>Listening first.</b> I asked each team what slowed them down, mapped the gaps and proposed fixes in cross-team meetings.</li>
    <li><b>KPIs.</b> I audited marketing and IT KPIs to find where things were getting stuck.</li>
  </ul>
</div>
<div><h2>Tools</h2>{tags([("hubspot","HubSpot"),(None,"Excel"),(None,"KPI tracking")])}</div>
""",
"montagu": f"""
<p class="lead">I interned with the deal team at Montagu's Paris office, a private equity firm. I focused on pharma and tech companies, mostly private SaaS and BPaaS businesses.</p>
<div>
  <h2>What I did</h2>
  <ul class="pts">
    <li>Market research and analysis to find companies, then short memos for the team.</li>
    <li>Expert calls to test the investment case.</li>
    <li>Helped prepare investment committee meetings and presented my work to an investment director.</li>
    <li>Learned the basics of LBOs, EBITDA multiples and commercial and financial due diligence.</li>
  </ul>
</div>
<div><h2>Skills</h2>{tags([(None,"Deal sourcing"),(None,"Market analysis"),(None,"Due diligence"),(None,"Excel")])}</div>
""",
}

for i, j in enumerate(JOBS):
    prev, nxt = (JOBS[i - 1] if i else None), (JOBS[i + 1] if i < len(JOBS) - 1 else None)
    pager = '<nav class="pager" aria-label="Other internships">'
    if prev:
        pager += f'<a href="{prev["slug"]}.html"><span>Previous</span><b>{prev["co"]}</b></a>'
    if nxt:
        pager += f'<a class="next" href="{nxt["slug"]}.html"><span>Next</span><b>{nxt["co"]}</b></a>'
    pager += "</nav>"
    body = f"""
<section class="hero short">{BEAM}<div class="wrap" style="width:100%"><div class="hero-copy">
  <a class="crumb" href="../experience.html">Experience</a>
  <div class="xhead">{logo(j, "../", "logo lg")}<h1>{j['co']}</h1></div>
  <div class="meta"><span>{j['role']}</span><span>{j['team']}</span><span>{j['dates']}</span><span>{j['place']}</span><span>{j['kind']}</span></div>
</div></div></section>
<section class="sec"><div class="wrap"><div class="detail">
{DETAIL[j['slug']]}
{pager}
</div></div></section>
"""
    page(f"experience/{j['slug']}.html", f"{j['co']} · Quentin Villet", f"Quentin Villet at {j['co']}.", body, "experience.html")

# ------------------------------------------------------------------ projects
projects = f"""
<section class="hero short">{BEAM}<div class="wrap" style="width:100%"><div class="hero-copy">
  <h1>Projects</h1>
  <p class="lede">Hackathons, side projects and class work. Click a project to open its code on GitHub.</p>
</div></div></section>
<section class="sec"><div class="wrap">
  <div class="grid two">{card(PROJECTS[0], wide=True)}{"".join(card(p) for p in PROJECTS[1:])}</div>
</div></section>
<section class="sec alt"><div class="wrap">
  <div class="head"><p class="label">smaller things</p><h2>Practice and coursework</h2></div>
  <div class="small">
    <div><h4>EY AI &amp; Data Challenge</h4><p>Forecasting water quality at 200+ river sites from satellite data.</p><span>Competition</span></div>
    <div><h4>Travel booking database</h4><p>A PostgreSQL database for flights, hotels and bookings, designed from scratch.</p><span>Databases class</span></div>
    <a href="https://github.com/QuentinVillet/Neural_Net-from-scratch" target="_blank" rel="noopener"><h4>Neural network from scratch</h4><p>Backpropagation written by hand in NumPy.</p><span>GitHub</span></a>
    <a href="https://github.com/QuentinVillet/SL_model-Heart-Failure" target="_blank" rel="noopener"><h4>Heart failure prediction</h4><p>Comparing classifiers on clinical data.</p><span>GitHub</span></a>
    <a href="https://github.com/QuentinVillet/KNN-from-scratch" target="_blank" rel="noopener"><h4>KNN from scratch</h4><p>Nearest neighbours without ML libraries.</p><span>GitHub</span></a>
    <a href="https://github.com/QuentinVillet/linreg-from-scratch" target="_blank" rel="noopener"><h4>Linear regression from scratch</h4><p>Closed form and gradient descent.</p><span>GitHub</span></a>
  </div>
</div></section>
"""
page("projects.html", "Projects · Quentin Villet", "Quentin Villet's projects.", projects, "projects.html")

# ------------------------------------------------------------------ studies & skills
LANGS = [("French", "100%", "Native"), ("English", "100%", "Native"), ("Spanish", "75%", "Business"), ("Chinese", "45%", "B1"), ("Italian", "25%", "A2")]
studies = f"""
<section class="hero short">{BEAM}<div class="wrap" style="width:100%"><div class="hero-copy">
  <h1>Studies &amp; skills</h1>
  <p class="lede">High school in Hong Kong, economics in Milan, a bootcamp in London, then engineering and business in Paris.</p>
</div></div></section>
<section class="sec"><div class="wrap">
  <div class="head"><p class="label">where I've studied</p><h2>Education</h2></div>
  <ul class="xp">{"".join(school_row(s) for s in SCHOOLS)}</ul>
</div></section>
<section class="sec alt"><div class="wrap skillsets">
  <div class="head right" style="margin-bottom:0"><p class="label">what I can do</p><h2>Skills</h2></div>
  <div><h3>Programming</h3>{tools_grid([("python","Python"),(None,"SQL"),("cplusplus","C++"),("r","R"),("swift","Swift"),(None,"Stata")]).replace('<span data-icon="None"></span>','')}</div>
  <div><h3>Machine learning</h3>{tools_grid([("pytorch","PyTorch"),("tensorflow","TensorFlow"),("scikitlearn","scikit-learn"),("huggingface","Hugging Face"),("opencv","OpenCV"),("ollama","Ollama"),("pandas","pandas"),("numpy","NumPy")])}</div>
  <div><h3>Data and cloud</h3>{tools_grid([("databricks","Databricks"),("googlebigquery","BigQuery"),("googlecloud","Google Cloud"),("postgresql","PostgreSQL"),("docker","Docker"),("fastapi","FastAPI"),("streamlit","Streamlit"),("looker","Looker Studio")])}</div>
  <div><h3>Building with AI</h3><div class="ai">
    <div><code>Claude Code</code><p>What I use to prototype quickly, including this website.</p></div>
    <div><code>frontend-design</code><p>For interfaces that don't look like templates.</p></div>
    <div><code>design-critique</code><p>For honest feedback on a layout before shipping it.</p></div>
    <div><code>accessibility-review</code><p>For checking contrast and keyboard use.</p></div>
  </div></div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="head"><p class="label">how I talk</p><h2>Languages</h2></div>
  <div class="langs">{"".join(f'<div class="lang"><span>{n}</span><i style="--v:{v}"></i><span>{l}</span></div>' for n, v, l in LANGS)}</div>
</div></section>
<section class="sec alt"><div class="wrap who">
  <div class="copy">
    <p class="label">outside of school</p>
    <h2>Sport, and a small business</h2>
    <p>I played rugby for Hong Kong's national team, and amateur football for FC Ravizza in Milan.</p>
    <p>Back in Hong Kong I set up a delivery network for the Eric Kayser bakeries, which made more than 10,000 HKD in profit a week. I also tutored girls aged 8 to 18 and helped raise over 300,000 HKD for children's charities.</p>
  </div>
  <figure class="orb"><img src="assets/quentin.jpg" alt="Quentin at the Great Wall of China Marathon" loading="lazy"><figcaption>At the Great Wall of China Marathon</figcaption></figure>
</div></section>
"""
page("studies.html", "Studies & skills · Quentin Villet", "Quentin Villet's studies, skills and languages.", studies, "studies.html")
print("built")
