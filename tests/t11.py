# Ansicht der Einkaufsliste: Einfach / Umfänglich / Manuell
from playwright.sync_api import sync_playwright
import os
errs=[]
def cnt(pg,sel):return pg.locator('#app '+sel+':not(.pv *)').count()
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.clear()");pg.reload()
    pg.click('[data-a=onname][data-skip]');pg.click('[data-a=onsize]')
    print('view page',pg.locator('[data-a=viewmode]').count(),'(3)')
    pg.click('[data-a=viewmode][data-v=simple]')
    print('preview simple: fav',pg.locator('.pv [data-a=fav]').count(),'shop',pg.locator('.pv [data-a=shopsel]').count(),'add',pg.locator('.pv [data-a=add]').count())
    pg.screenshot(path='s11a.png',full_page=True)
    pg.click('[data-a=onview]');pg.click('[data-a=ontour][data-v="0"]');pg.click('[data-a=onset][data-v="0"]')
    pg.fill('#dn','Milch');pg.click('[data-a=add]')
    print('list simple: fav',cnt(pg,'[data-a=fav]'),'fire',cnt(pg,'[data-fire]'),'shop',cnt(pg,'[data-a=shopsel]'),'cam',cnt(pg,'.camb'),'bar',cnt(pg,'#shopbtn'),'check',cnt(pg,'[data-a=check]'),'recent',pg.inner_text('#app').count('Letzte Produkte'))
    pg.click('#hamb');print('menu favs',pg.locator('.menu [data-v=favs]').count())
    pg.click('[data-a=nav][data-v=settings]');pg.click('[data-a=sub][data-v=liste]')
    pg.click('[data-chk=v_fav]');pg.wait_for_timeout(100)
    print('after fav on: mode manual',pg.locator('[data-a=viewmode][data-v=manual].pri').count(),'pv fav',pg.locator('.pv [data-a=fav]').count())
    print('simple: remind section hidden',pg.locator('#remh').count())
    pg.click('[data-a=viewmode][data-v=full]')
    print('full: remind section',pg.locator('#remh').count(),'nav switch',pg.locator('[data-chk=v_nav]').is_checked())
    pg.select_option('[data-chg=remMode]','ios');pg.wait_for_timeout(100);pg.click('[data-chk=remSc]');pg.wait_for_timeout(100);print('shortcut name field',pg.locator('[data-chg=scName]').count())
    print('full: pv shop',pg.locator('.pv [data-a=shopsel]').count(),'fire',pg.locator('.pv [data-fire]').count())
    pg.click('[data-a=nav][data-v=list]');print('list full: fav',cnt(pg,'[data-a=fav]'),'cam',cnt(pg,'.camb'),'recent',pg.inner_text('#app').count('Letzte Produkte'))
    # tour in simple mode skips hidden steps
    pg.evaluate("var s=JSON.parse(localStorage.getItem('sebu.v1'));s.set.view='simple';s.set.show={fav:false,shop:false,cam:false,bar:false,recent:false};s.set.dm='off';localStorage.setItem('sebu.v1',JSON.stringify(s))");pg.reload()
    pg.click('#hamb');pg.click('[data-a=nav][data-v=settings]');pg.click('[data-a=sub][data-v=tour]');pg.click('[data-a=tour][data-v=app]');pg.wait_for_timeout(200)
    print('app tour simple:',pg.inner_text('.tc .small.mute'),'(weniger als 47)')
    b.close()
print(errs)
