# Hilfe-Suche im Menü
from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    c=b.new_context(viewport={'width':390,'height':800});pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n21',greet:'off'}}))");pg.reload()
    pg.click('#hamb');print('search on top',pg.locator('.menu #msq').count())
    for q in ['Erinnerung','Schrift','Drehrad','QR','zzzq']:
        pg.fill('#msq','');pg.type('#msq',q);print(q,pg.locator('#msres .hres').count(),[x.replace('\n',' | ') for x in pg.locator('#msres .hres').all_inner_texts()[:4]])
    pg.fill('#msq','');pg.type('#msq','Schrift');pg.click('#msres .hres >> nth=0');pg.wait_for_timeout(500)
    print('went to',pg.inner_text('h2'),'highlight',pg.locator('.hl').count())
    pg.screenshot(path='/tmp/claude-0/shots/s38.png')
    c.close();b.close()
print(errs)
