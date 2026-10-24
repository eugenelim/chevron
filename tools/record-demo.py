# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Re-record docs/demo.gif and docs/screenshot.png from index.html.

Usage:  uv run tools/record-demo.py [frame-name ...]

Each frame is a copy of index.html with a short script injected that drives
the UI (keys, clicks), screenshotted by headless Edge or Chrome at 1280x800.
The frames are then captioned and stitched into the GIF. Pass frame names to
re-render only those (the GIF is still built from every frame on disk).
Frames are kept in tools/.frames/ (git-ignored).
"""
import os, shutil, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, OUT = os.path.join(ROOT, 'index.html'), os.path.join(ROOT, 'docs')
WORK = os.path.join(ROOT, 'tools', '.frames')
BROWSERS = ['/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            'microsoft-edge', 'google-chrome', 'chromium']
FONT = '/System/Library/Fonts/Helvetica.ttc'

# Injected before the app: no animations, no popups, and small helpers.
# K(key, opts) presses a key, Q(text) types into search, AT(ms, fn) runs fn
# ms after the page has settled.
HELPERS = """<style>*{transition:none!important}</style><script>window.open=()=>null;window.prompt=()=>null;window.confirm=()=>true;
const K=(k,o={})=>document.dispatchEvent(new KeyboardEvent('keydown',{key:k,bubbles:true,...o}));
const Q=(v)=>{const q=document.querySelector('#q');q.value=v;q.dispatchEvent(new Event('input'));};
const AT=(ms,f)=>setTimeout(f,ms+3500);</script>"""

# (name, mode, theme, script, caption) in GIF order
FRAMES = [
    ('01-home', 'dark', 'cocoa', "", 'Your links in cards; each clock shows its weather top left'),
    ('02-shortcut', 'dark', 'cocoa', "AT(3250,()=>K('g'))", 'Type a shortcut to open a link (here "g…"): matches light up'),
    ('03-search', 'dark', 'cocoa', "AT(800,()=>{K('k',{ctrlKey:true});Q('tag:ai')})", 'Ctrl/Cmd K searches everything, with filters like tag:ai'),
    ('04-finder', 'dark', 'cocoa', "AT(800,()=>{K('k',{ctrlKey:true});Q('yt lofi beats')})", 'Search the web with finders: yt, g, gh, $ and more'),
    ('05-commands', 'dark', 'cocoa', "AT(800,()=>{K('k',{ctrlKey:true});Q(':theme')})", 'Type : for commands: themes, exports, widgets, pages'),
    ('06-news', 'dark', 'cocoa', "AT(500,()=>K('2'))", 'Press 1–9 to switch pages: News'),
    ('07-finance', 'dark', 'cocoa', "AT(500,()=>K('3'))", '…and Finance'),
    ('07b-rename', 'dark', 'cocoa', "AT(500,()=>{K('3');const t=document.querySelector('#pages [data-droppage]:nth-child(3)');t.dispatchEvent(new MouseEvent('dblclick',{bubbles:true}));const i=document.querySelector('#pages .tab-edit');i.value='Markets';i.dispatchEvent(new Event('input'));})", 'Double-click a page tab to rename it'),
    ('08b-weather', 'dark', 'cocoa', "AT(500,()=>document.querySelector('#clocks .clock').click())", "Click a clock for that city's hourly weather"),
    ('08c-weather-week', 'dark', 'cocoa', "AT(500,()=>{document.querySelector('#clocks .clock').click();AT(-3400,()=>document.querySelector('[data-wxv=week]').click())})", '…then switch to the 7-day forecast'),
    ('08-editor', 'dark', 'cocoa', "AT(800,()=>{K('k',{ctrlKey:true});Q('gmail');document.querySelector('#q').dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',shiftKey:true,bubbles:true}));})", 'Edit any link in the side panel; changes save as you type'),
    ('09-bookmarks', 'dark', 'cocoa', "AT(800,()=>K('B',{shiftKey:true}))", 'Bookmarks view: filters, sorting, health scores, bulk actions'),
    ('10-tags', 'dark', 'cocoa', "AT(800,()=>{K('/');AT(100,()=>{const t=[...document.querySelectorAll('[data-tg]')].find(x=>x.dataset.tg==='ai');t&&t.click();})})", 'Tag cloud: browse, rename and merge tags across pages'),
    ('11-look', 'dark', 'cocoa', "AT(800,()=>K('A',{shiftKey:true}))", 'Look studio: 13 themes, card styles, fonts and backdrops'),
    ('12-light', 'light', 'nightcity', "", 'Every theme has a light and a dark version'),
    ('13-light-finance', 'light', 'ember', "AT(500,()=>K('3'))", 'Light mode, another theme'),
    ('14-cheat', 'light', 'nightcity', "AT(800,()=>K('?'))", 'Press ? for every keyboard shortcut'),
]


def browser():
    for b in BROWSERS:
        if os.path.exists(b) or shutil.which(b):
            return b
    sys.exit('Need Microsoft Edge or Google Chrome installed')


def render(only):
    exe, base = browser(), open(SRC, encoding='utf-8').read()
    os.makedirs(WORK, exist_ok=True)
    for name, mode, theme, js, _ in FRAMES:
        if only and name not in only:
            continue
        html = base.replace('"mode": "system"', f'"mode": "{mode}"').replace('"theme": "cocoa"', f'"theme": "{theme}"')
        html = html.replace('<head>', '<head>' + HELPERS, 1).replace('</body>', f'<script>{js}</script></body>')
        page, png = os.path.join(WORK, name + '.html'), os.path.join(WORK, name + '.png')
        open(page, 'w', encoding='utf-8').write(html)
        if os.path.exists(png):
            os.remove(png)
        profile = os.path.join(WORK, 'profile-' + name)  # fresh localStorage per frame
        shutil.rmtree(profile, ignore_errors=True)
        subprocess.run([exe, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--user-data-dir={profile}',
                        '--window-size=1280,800', '--virtual-time-budget=7000', f'--screenshot={png}', 'file://' + page],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        shutil.rmtree(profile, ignore_errors=True)
        print(name, 'ok' if os.path.exists(png) else 'FAILED')


def stitch():
    W, H = 1040, 650
    font = ImageFont.truetype(FONT, 22) if os.path.exists(FONT) else ImageFont.load_default(22)
    frames = []
    for name, *_, cap in FRAMES:
        im = Image.open(os.path.join(WORK, name + '.png')).convert('RGB').resize((W, H), Image.LANCZOS)
        d = ImageDraw.Draw(im, 'RGBA')
        tw, pad = d.textlength(cap, font=font), 16
        x0, y0 = (W - tw) / 2 - pad, H - 64
        d.rounded_rectangle([x0, y0, x0 + tw + 2 * pad, y0 + 42], radius=21, fill=(20, 20, 28, 235), outline=(255, 255, 255, 70), width=1)
        d.text((x0 + pad, y0 + 8), cap, font=font, fill=(255, 255, 255))
        frames.append(im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE))
    gif = os.path.join(OUT, 'demo.gif')
    frames[0].save(gif, save_all=True, append_images=frames[1:], duration=[2600] + [2200] * (len(frames) - 1), loop=0, optimize=True)
    shot = os.path.join(OUT, 'screenshot.png')
    Image.open(os.path.join(WORK, '01-home.png')).convert('RGB').save(shot, optimize=True)
    for f in (gif, shot):
        print(os.path.relpath(f, ROOT), round(os.path.getsize(f) / 1024), 'KB')


if __name__ == '__main__':
    render(sys.argv[1:])
    stitch()
