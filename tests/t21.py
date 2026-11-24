# Antwort-Seite für den Händler-Brief
from playwright.sync_api import sync_playwright
import os,urllib.parse as u
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/antwort.html?an=Migros')
    print('rows',pg.locator('.row').count(),'send off',pg.locator('#send.off').count())
    for i,v in enumerate(['Ja','Nein','Ja','Ja']):pg.click('.pill[data-i="%d"][data-v="%s"]'%(i,v))
    pg.fill('#bm','Gerne Termin');pg.fill('#nm','Test Person')
    h=pg.get_attribute('#send','href');body=u.unquote(h.split('body=')[1])
    print('send on',pg.locator('#send.off').count()==0,'to',h.split('?')[0],'subject',u.unquote(h.split('subject=')[1].split('&')[0]))
    print(body.replace('\n',' | '))
    pg.screenshot(path='s21.png',full_page=True)
    b.close()
print(errs)
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/antwort.html?an=Coop');print('coop row',pg.locator('.row .t').nth(2).inner_text(),'title',pg.inner_text('#ti'))
    b.close()
print(errs)
