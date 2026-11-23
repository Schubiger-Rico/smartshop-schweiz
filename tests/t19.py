# Mehr Kategorien, bessere automatische Kategorie, neue Kategorie-Auswahl
from playwright.sync_api import sync_playwright
import os
errs=[]
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
want={'Erdbeerjoghurt':'Joghurt','Paprikapulver':'Gewürze','Rapsöl':'Öl & Essig','Kokosmilch':'Asia','Sojasauce':'Asia','Tortillas':'Mexiko & Tex-Mex','Hafermilch':'Milchalternativen','Windeln':'Windeln','Tomatensauce':'Saucen','Schweinefleisch':'Schwein','Rösti':'Pommes & Kartoffelprodukte','Rivella':'Süssgetränke','Zwiebeln':'Kartoffeln & Zwiebeln','Tofu':'Asia','Müesli':'Müesli & Frühstück','Vanillezucker':'Mehl & Backzutaten'}
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html')
    # bestehender Nutzer mit alten Kategorien (ohne neue) → Migration
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},cats:[{id:'m0',name:'Obst & Gemüse',parentId:null,icon:'🥦',sortOrder:0},{id:'m13',name:'Übrige',parentId:null,icon:'📦',sortOrder:13}]}))");pg.reload()
    ids=[c['id'] for c in st(pg)['cats']];print('migrated asia',('m14s0' in ids),'übrige last',sorted(st(pg)['cats'],key=lambda c:c['sortOrder'] if not c.get('parentId') else 1e9)[[c for c in st(pg)['cats'] if not c.get('parentId')].__len__()-1]['id'])
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    for n in want:pg.fill('#dn',n);pg.click('[data-a=add]')
    cats={c['id']:c['name'] for c in st(pg)['cats']};bad={}
    for i in st(pg)['items']:
        g=cats.get(i.get('sub') or i.get('cat'))
        if g!=want[i['name']]:bad[i['name']]=g
    print('auto category wrong:',bad)
    pg.locator('.card[data-swk=i] .ic').first.click()
    print('picker mains',pg.locator('.sheet .catm').count(),'open subs',pg.locator('.sheet .catpk.sub').count())
    pg.fill('#catq','asia');print('search asia',pg.locator('.sheet .catpk').all_inner_texts())
    pg.screenshot(path='s19.png')
    pg.fill('#catq','');pg.click('[data-a=catopen][data-id=m14]');print('opened subs',pg.locator('.sheet .catpk.sub').count()>=5)
    b.close()
print(errs)
