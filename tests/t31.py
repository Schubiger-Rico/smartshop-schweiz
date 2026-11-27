# Weiterempfehlen: Menüpunkt, QR-Code, Link kopieren
from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch()
    c=b.new_context(viewport={'width':390,'height':800},permissions=['clipboard-read','clipboard-write']);pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n20',greet:'off'}}))");pg.reload()
    pg.click('#hamb');items=pg.locator('.menu > button').all_inner_texts();print('after settings',[x.replace('\n',' ') for x in items][-3:])
    pg.click('.menu [data-v=recommend]');print('qr loaded',pg.evaluate("document.getElementById('qrimg').naturalWidth>100"))
    pg.click('[data-a=reccopy]');pg.wait_for_timeout(300);print('copied',pg.evaluate("navigator.clipboard.readText()"))
    pg.screenshot(path='/tmp/claude-0/shots/s37.png')
    c.close();b.close()
import qrcode
print(errs)
