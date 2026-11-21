from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    n=pg.evaluate("(function(){return tourSteps('all').length})()") if False else None
    pg.click('#hamb');pg.click('[data-a=nav][data-v=settings]');pg.click('[data-a=sub][data-v=tour]');pg.click('[data-a=tour][data-v=set]')
    miss=[];seen=0
    for i in range(200):
        if pg.locator('.tc').count()==0:break
        pg.wait_for_timeout(200)
        txt=pg.inner_text('.tc .small.mute');x=pg.inner_text('.tc p')
        hl=pg.locator('.hl').count()
        if hl==0:miss.append((txt,x[:50]))
        seen+=1
        if i==-1:
            # test ro: click highlighted menu item must not navigate; test Mehr
            if pg.locator('[data-a=tmore]').count():pg.click('[data-a=tmore]');print('more text shown',pg.locator('.tc p').count())
            pg.click('.hl',force=True);print('after click on ro still step',pg.inner_text('.tc .small.mute'))
            pg.click('body',position={'x':5,'y':300},force=True);print('oops1:',pg.inner_text('.toast,#toast') if pg.locator('.toast,#toast').count() else '?')
        if pg.locator('[data-a=tnext]').count():pg.click('[data-a=tnext]')
        else:
            if pg.locator('#dn').count() and pg.locator('.hl #dn').count():
                pg.fill('#dn','Milch');pg.click('[data-a=add]')
            else: pg.click('.hl')
    print('steps',seen,'missing',miss)
    print(errs)
    b.close()
