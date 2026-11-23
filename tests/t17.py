# Nur Symbole, Erklärung beim Gedrückthalten, Einstellungen
from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    print('start symbol only',repr(pg.inner_text('#shopbtn')))
    bb=pg.locator('[data-a=shopstart]').bounding_box();pg.mouse.move(bb['x']+10,bb['y']+10);pg.mouse.down();pg.wait_for_timeout(2200)
    print('help',pg.inner_text('#toast')[:30]);pg.mouse.up();pg.wait_for_timeout(200)
    print('click suppressed (no shop started)',pg.locator('[data-a=shopend]').count()==0)
    pg.click('#hamb');pg.click('.menu [data-v=settings]');pg.click('[data-a=sub][data-v=look]')
    pg.click('[data-chk=btnText]');pg.click('[data-chk=lpHelp]');pg.click('[data-a=nav][data-v=list]')
    print('with text',repr(pg.inner_text('#shopbtn')))
    bb=pg.locator('[data-a=gpsrefresh]').bounding_box();pg.evaluate("document.getElementById('toast').textContent=''");pg.mouse.move(bb['x']+10,bb['y']+10);pg.mouse.down();pg.wait_for_timeout(2200);print('help off toast',repr(pg.inner_text('#toast')[:20]));pg.mouse.up()
    b.close()
print(errs)
