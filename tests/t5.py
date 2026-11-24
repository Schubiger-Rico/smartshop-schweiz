from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    pg.click('#hamb');print('Läden in main menu',pg.locator('.menu [data-a=nav][data-v=shops]').count(),'Aktionen',pg.locator('.menu [data-a=nav][data-v=deals]').count());pg.click('[data-a=nav][data-v=settings]')
    pg.click('[data-a=sub][data-v=price]')
    for m in ['auto','off','manual']:
        pg.select_option('select[data-chg=dm]',m)
        pg.click('#hamb');pg.click('[data-a=nav][data-v=list]')
        pg.fill('#dn','Brot');pg.click('[data-a=add]')
        print(m,'fire btns',pg.locator('.card .fire').count(),'on',pg.locator('.card .fire.on').count())
        pg.click('#hamb');print(' Aktionen menu',pg.locator('.menu [data-a=nav][data-v=deals]').count());pg.click('[data-a=nav][data-v=settings]');pg.click('[data-a=sub][data-v=price]')
        pg.evaluate("document.querySelectorAll('.card').forEach(c=>c)")
    b.close()
print(errs)
# Aktionshinweis mit ✕ ausblenden
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{dm:'always'}}))");pg.reload()
    pg.fill('#dn','Butter');pg.click('[data-a=add]')
    n=pg.locator('[data-a=dealx]').count()
    if n:pg.click('[data-a=dealx]');pg.reload()
    print('deal banner x',n,'after dismiss+reload',pg.locator('[data-a=dealx]').count())
    b.close()
print(errs)
