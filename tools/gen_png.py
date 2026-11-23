import re,shutil
from playwright.sync_api import sync_playwright
import os
from pathlib import Path
R=str(Path(__file__).resolve().parent.parent)+'/'
def svg_size(p):
    vb=re.search(r'viewBox="0 0 (\d+) (\d+)"',open(p).read()); return int(vb.group(1)),int(vb.group(2))
with sync_playwright() as p:
    b=p.chromium.launch()
    def svg_png(src,out,width):
        w,h=svg_size(R+src); H=round(width*h/w)
        pg=b.new_page(viewport={'width':width,'height':H})
        pg.goto('file://'+R+src); pg.wait_for_timeout(300)
        pg.screenshot(path=R+out,omit_background=True); pg.close()
    # logos e favicons vêm prontos do pacote v1 (brand/logo e brand/png); aqui só as peças
    O='brand/png/'
    def page_png(src,out,w,h,wait=600):
        pg=b.new_page(viewport={'width':w,'height':h}); pg.goto('file://'+R+src); pg.wait_for_timeout(wait)
        pg.screenshot(path=R+out); pg.close()
    page_png('brand/applications/og.html',O+'og-preview-social.png',1200,630)
    shutil.copy(R+O+'og-preview-social.png',R+'assets/img/og.png')
    page_png('brand/applications/linkedin-banner.html',O+'linkedin-banner.png',1584,396)
    # prévia local da assinatura (troca a URL publicada pelo arquivo local)
    h=open(R+'brand/applications/assinatura-email.html').read().replace('https://leandrogoulart.github.io/GoulartInfoSolutions/brand/png/','file://'+R+'brand/png/')
    open(R+'brand/applications/_prev.html','w').write(h)
    pg=b.new_page(viewport={'width':520,'height':150}); pg.goto('file://'+R+'brand/applications/_prev.html'); pg.wait_for_timeout(400)
    pg.screenshot(path=R+O+'assinatura-email-preview.png'); pg.close()
    b.close()
os.remove(R+'brand/applications/_prev.html')
print(sorted(os.listdir(R+'brand/png')))
