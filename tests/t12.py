# Test-Hinweise «🚧» in unfertigen Bereichen
from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    print('list no banner',pg.locator('.tb').count())
    for v in ['deals','ideas']:
        pg.click('#hamb');pg.click('.menu [data-v=%s]'%v);print(v,pg.locator('.tbh').inner_text())
    pg.screenshot(path='s12.png')
    pg.click('#hamb');pg.click('[data-a=more]');pg.click('.menu [data-v=events]');print('events',pg.locator('.tb').count())
    pg.click('#hamb');pg.click('.menu [data-v=settings]');pg.click('[data-a=sub][data-v=plan]');print('plan',pg.locator('.tb').count())
    pg.click('[data-a=sub][data-v=main]');pg.click('[data-a=sub][data-v=look]');pg.click('[data-chk=testBan]')
    pg.click('#hamb');pg.click('.menu [data-v=deals]');print('after off',pg.locator('.tb').count())
    b.close()
print(errs)
