# Produktfoto
from playwright.sync_api import sync_playwright
import os
errs=[]
IMG=os.path.join(os.getcwd(),'icon-180.png')
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{newsSeen:'n08'}}))");pg.reload()
    pg.fill('#dn','Pizzamehl');pg.set_input_files('[data-chg=photodraft]',IMG);pg.wait_for_timeout(400)
    print('draft thumb',pg.locator('.phb img').count(),'name kept',pg.input_value('#dn'))
    pg.click('[data-a=add]');pg.wait_for_timeout(200)
    print('photo stored',list((st(pg).get('photos') or {}).keys()),'card img',pg.locator('.card[data-swk=i] .ic.ph img').count())
    pg.click('.card[data-swk=i] .ic.ph');print('viewer',pg.locator('.sheet img').count(),'cat btn',pg.locator('.sheet [data-a=catpick]').count())
    pg.click('[data-a=photodel]');print('removed',pg.locator('.card[data-swk=i] .ic.ph').count(),'icon back',pg.locator('.card[data-swk=i] .ic').count())
    pg.screenshot(path='s23.png')
    b.close()
print(errs)
