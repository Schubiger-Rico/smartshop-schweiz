# Mehr Kategorien, bessere automatische Kategorie, neue Kategorie-Auswahl
from playwright.sync_api import sync_playwright
import os
errs=[]
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
want={'Erdbeerjoghurt':'Joghurt','Paprikapulver':'Gewürze','Rapsöl':'Öl & Essig','Kokosmilch':'Asia','Sojasauce':'Asia','Tortillas':'Mexiko & Tex-Mex','Hafermilch':'Milchalternativen','Windeln':'Windeln','Tomatensauce':'Saucen','Schweinefleisch':'Schwein','Rösti':'Pommes & Kartoffelprodukte','Rivella':'Süssgetränke','Zwiebeln':'Kartoffeln & Zwiebeln','Tofu':'Asia','Müesli':'Müesli & Flocken','Essig':'Öl & Essig','Nutella':'Brotaufstrich','Honig':'Konfitüre & Honig','Vanillezucker':'Mehl & Backzutaten'}
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html')
    # bestehender Nutzer mit alten Kategorien (ohne neue) → Migration
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},cats:[{id:'m0',name:'Obst & Gemüse',parentId:null,icon:'🥦',sortOrder:0},{id:'m13',name:'Übrige',parentId:null,icon:'📦',sortOrder:13}]}))");pg.reload()
    ids=[c['id'] for c in st(pg)['cats']];print('migrated asia',('m14s0' in ids),'übrige last',sorted(st(pg)['cats'],key=lambda c:c['sortOrder'] if not c.get('parentId') else 1e9)[[c for c in st(pg)['cats'] if not c.get('parentId')].__len__()-1]['id'])
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},items:[{id:'x',name:'Granola',qty:1,unit:'Stk.',cat:'m4',sub:'m4s8'}]}))");pg.reload()
    x=st(pg)['items'][0];print('moved to Frühstück',x['cat'],x['sub'],'m4 name',[c['name'] for c in st(pg)['cats'] if c['id']=='m4'])
    pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    for n in want:pg.fill('#dn',n);pg.click('[data-a=add]')
    cats={c['id']:c['name'] for c in st(pg)['cats']};bad={}
    for i in st(pg)['items']:
        g=cats.get(i.get('sub') or i.get('cat'))
        if g!=want[i['name']]:bad[i['name']]=g
    print('auto category wrong:',bad)
    names=[t.split('\n')[0] for t in pg.locator('.card[data-swk=i] .nm').all_inner_texts()];oi=[n for n in names if n in('Essig','Rapsöl')];print('oil+vinegar adjacent',abs(names.index('Essig')-names.index('Rapsöl'))==1)
    bb=pg.locator('.card[data-swk=i]',has_text='Essig').locator('.ic').bounding_box();pg.mouse.move(bb['x']+5,bb['y']+5);pg.mouse.down();pg.wait_for_timeout(2200);print('belongs',pg.inner_text('#toast'));pg.mouse.up();pg.wait_for_timeout(300)
    if pg.locator('.sheet').count():pg.mouse.click(5,5)
    pg.locator('.card[data-swk=i] .ic').first.click()
    print('picker mains',pg.locator('.sheet .catm').count(),'open subs',pg.locator('.sheet .catpk.sub').count())
    pg.fill('#catq','asia');print('search asia',pg.locator('.sheet .catpk').all_inner_texts())
    pg.screenshot(path='s19.png')
    pg.fill('#catq','');pg.click('[data-a=catopen][data-id=m14]');print('opened subs',pg.locator('.sheet .catpk.sub').count()>=5)
    b.close()
print(errs)
