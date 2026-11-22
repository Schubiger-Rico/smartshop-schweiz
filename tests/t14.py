# Notfall / dringend
from playwright.sync_api import sync_playwright
import os
errs=[]
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    for n in ['Äpfel','Brot']:pg.fill('#dn',n);pg.click('[data-a=add]')
    pg.fill('#dn','Windeln');pg.click('[data-a=urgtog][data-id=draft]');print('draft kept',pg.input_value('#dn'))
    pg.click('[data-a=shopsel][data-id=draft]');pg.click('[data-a=shtog][data-v=Lidl]');pg.click('[data-a=shok]');pg.click('[data-a=add]')
    names=pg.locator('.card[data-swk=i] .nm').all_inner_texts();print('first',names[0][:7],'urg cards',pg.locator('.card.urg').count(),'(store item visible)')
    pg.screenshot(path='s14.png')
    pg.click('#shopbtn');pg.wait_for_timeout(100)
    if pg.locator('[data-a=shopstart]').count()==0 and pg.locator('.sheet').count():pg.locator('.sheet button').first.click()
    pg.wait_for_timeout(200);pg.click('[data-a=shopend]') if pg.locator('[data-a=shopend]').count() else None;pg.wait_for_timeout(200)
    print('end banner',pg.inner_text('#app').count('Dringend noch offen'))
    if pg.locator('[data-a=urgok]').count():pg.click('[data-a=urgok]')
    pg.click('.card.urg [data-a=urgtog]');print('after untoggle urg',pg.locator('.card.urg').count())
    pg.click('#hamb');pg.click('.menu [data-v=settings]');pg.click('[data-a=sub][data-v=liste]');pg.click('[data-a=viewmode][data-v=simple]')
    pg.click('[data-a=nav][data-v=list]');print('simple no urg btn',pg.locator('[data-a=urgtog][data-id=draft]').count())
    b.close()
print(errs)
