from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    pg.fill('#dn','Milch');pg.click('[data-a=add]');pg.fill('#dn','Zahnpasta');pg.click('[data-a=add]')
    pg.click('#hamb');pg.click('[data-a=nav][data-v=settings]');print('Liste btn main',pg.locator('#app [data-a=nav][data-v=list]').count())
    pg.click('[data-a=sub][data-v=price]');print('Liste btn sub',pg.locator('#app [data-a=nav][data-v=list]').count())
    pg.select_option('select[data-chg=dm]','always')
    pg.click('#app [data-a=nav][data-v=list]');print('view list',pg.locator('#dn').count(),'fire btns',pg.locator('.card .fire').count(),'names',pg.locator('.card .nm').all_inner_texts())
    b.close()
print(errs)
