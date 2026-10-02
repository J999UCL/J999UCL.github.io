"""Build the plain portfolio and CV-compatible project URLs."""
from pathlib import Path
from html import escape as e
import json
ROOT = Path(__file__).resolve().parent.parent
projects = json.loads((ROOT / 'projects.json').read_text())

def page(title, body, base='', nav=True, canonical=None, description='Jeet Thakwani — Computer Science at UCL.'):
    navigation = f'<nav aria-label="Main navigation"><a href="{base}index.html">Home</a><a href="{base}projects/">Projects</a><a href="{base}CV_Jeet_Thakwani.pdf">CV</a></nav>' if nav else ''
    canonical_tag = f'<link rel="canonical" href="https://jeet.thakwani.com{e(canonical, quote=True)}">' if canonical else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description, quote=True)}">
{canonical_tag}
<link rel="stylesheet" href="{base}plain.css">
</head>
<body>{navigation}<main>{body}</main></body>
</html>
'''

home='''<h1>Jeet Thakwani</h1>
<p>Computer Science at University College London.</p>
<ul class="home-links">
<li><a href="projects/">Projects</a></li>
<li><a href="https://github.com/J999UCL">GitHub</a></li>
<li><a href="https://www.linkedin.com/in/jeet-thakwani-41b560305">LinkedIn</a></li>
<li><a href="CV_Jeet_Thakwani.pdf">CV</a></li>
</ul>
<p class="contact"><a href="mailto:jeetucl@hotmail.com">jeetucl@hotmail.com</a></p>
<p class="small"><a href="about.html">About</a></p>'''
(ROOT/'index.html').write_text(page('Jeet Thakwani',home,nav=False,canonical='/'))
items=[]
for p in projects:
    fragment_path=ROOT/'content'/f'{p["slug"]}.html'
    if not fragment_path.is_file():
        raise FileNotFoundError(f'Missing project write-up: {fragment_path}')
    fragment=fragment_path.read_text()
    items.append(f'<li><h2><a href="{p["slug"]}/">{e(p["title"])}</a></h2><p>{e(p["subtitle"])}</p></li>')
    body=f'''<article><header class="article-header"><h1>{e(p['title'])}</h1><p class="muted">{e(p['tags'])}</p></header>{fragment}<p class="back-projects"><a href="../">← All projects</a></p></article>'''
    for slug in [p['slug'],*p.get('aliases',[])]:
        folder=ROOT/'projects'/slug;folder.mkdir(parents=True,exist_ok=True)
        (folder/'index.html').write_text(page(p['title']+' — Jeet Thakwani',body,'../../',canonical=f'/projects/{p["slug"]}/',description=p['subtitle']))
listing='<h1>Projects</h1><p class="muted">Notes on what I built, how it works, and what I learned.</p><ul class="project-list">'+''.join(items)+'</ul>'
(ROOT/'projects'/'index.html').write_text(page('Projects — Jeet Thakwani',listing,'../',canonical='/projects/'))
about='''<h1>About</h1>
<p>I’m studying MEng Computer Science at University College London (2024–2028).</p>
<p>My projects span computer vision, reinforcement learning, language models, and developer tools.</p>
<p>I represented Ghana at the International Mathematical Olympiad in 2023. At UCL, I’ve also worked as a programming teaching assistant and Lead Department Representative.</p>
<p><a href="CV_Jeet_Thakwani.pdf">View my CV</a> or <a href="mailto:jeetucl@hotmail.com">email me</a>.</p>'''
(ROOT/'about.html').write_text(page('About — Jeet Thakwani',about,canonical='/about.html'))
(ROOT/'work.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="0;url=projects/"><title>Projects — Jeet Thakwani</title></head><body><a href="projects/">Projects</a></body></html>''')
(ROOT/'404.html').write_text(page('Page not found — Jeet Thakwani','<h1>Page not found</h1><p><a href="/">Back to the homepage</a></p>','/'))
print(f'Built {len(projects)} write-ups and {sum(len(p.get("aliases",[])) for p in projects)} CV-compatible aliases.')
