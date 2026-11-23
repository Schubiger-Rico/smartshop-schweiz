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
# Schriftgrösse − / +
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.clear()");pg.reload()
    pg.click('[data-a=onname][data-skip]');pg.click('[data-a=fsup]');pg.click('[data-a=fsup]');print('fs shown',pg.inner_text('#fsv'))
    pg.screenshot(path='s17.png');b.close()
print(errs)
# Hinweis verschwindet nach 3× Wischen, Letzte Produkte ohne Auswahl in der Liste
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    for n in ['Brot','Käse','Milch','Butter']:pg.fill('#dn',n);pg.click('[data-a=add]')
    print('hint before',pg.inner_text('#app').count('nach links wischen'),'recent selects in list',pg.locator('#app [data-chg=recN]').count())
    for i in range(3):
        bb=pg.locator('.card[data-swk=i]').first.bounding_box();y=bb['y']+bb['height']/2
        pg.mouse.move(bb['x']+bb['width']-20,y);pg.mouse.down();pg.mouse.move(bb['x']+20,y,steps=8);pg.mouse.up();pg.wait_for_timeout(500)
    print('hint after 3 swipes',pg.inner_text('#app').count('nach links wischen'),pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1')).set.swipeN"),len(pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1')).items")))
    b.close()
print(errs)
