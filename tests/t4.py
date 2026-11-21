from playwright.sync_api import sync_playwright
import os
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{gps:'off'},mine:[{name:'Beck Z',lat:1,lon:1}]}))");pg.reload()
    pg.fill('#dn','Milch');pg.click('[data-a=add]')
    pg.fill('#dn','Brot');pg.click('[data-a=shopsel][data-id=draft]')
    print('own store in picker',pg.locator('[data-a=shtog][data-v="Beck Z"]').count())
    pg.click('[data-a=shtog][data-v=Lidl]');pg.click('[data-a=shok]');pg.click('[data-a=add]')
    print('cards main (expect 1)',pg.locator('.card[data-swk=i]').count(),'hint',pg.locator('[data-a=nav][data-v=shops]').count())
    pg.click('[data-a=nav][data-v=shops]');print('shops view cards',pg.locator('.card[data-swk=i]').count(),'h3',pg.locator('#app h3').all_inner_texts())
    pg.click('#hamb');print('menu shops',pg.locator('[data-a=nav][data-v=shops]').count())
    pg.click('[data-a=nav][data-v=settings]');pg.click('[data-a=sub][data-v=stores]')
    pg.fill('#cn','Testladen');pg.click('[data-a=chainadd]');print('Manor row',pg.locator('[data-a=chaindel]').count())
    pg.click('[data-mine="0"]');print('off',pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1')).mine[0].off"))
    pg.click('[data-a=chaindel]');print('after del',pg.locator('[data-a=chaindel]').count())
    pg.screenshot(path='s8.png')
    # synonyms
    print(pg.evaluate("1"))
    b.close()
print(errs)
