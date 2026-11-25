# Schnellstart-Knopf vor dem Einkaufswagen
from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    c=b.new_context(viewport={'width':390,'height':800});pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n15'}}))");pg.reload()
    print('off by default',pg.locator('.qkb').count()==0)
    pg.click('#hamb');pg.click('.menu [data-v=settings]');pg.click('[data-a=sub][data-v=liste]')
    pg.select_option('[data-chg=quick]','favs')
    pg.click('[data-a=nav][data-v=list] >> nth=0');pg.wait_for_timeout(300)
    order=pg.evaluate("Array.from(document.querySelectorAll('.qkb,[data-a=shopstart]')).map(function(e){return e.dataset.a})")
    print('before cart',order)
    pg.screenshot(path='/tmp/claude-0/shots/s27.png')
    pg.click('.qkb');print('opens favs','Favoriten' in pg.inner_text('#app'))
    c.close();b.close()
print(errs)
