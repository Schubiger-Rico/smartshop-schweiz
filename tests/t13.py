# Rückgängig, automatische Sicherung (Gerät + Firebase gemockt), Strichcode (Open Food Facts gemockt)
from playwright.sync_api import sync_playwright
import os,json
errs=[];db={}
def fb(route):
    r=route.request;k=r.url.split('.com')[1].split('?')[0]
    if r.method=='PUT':db[k]=json.loads(r.post_data);route.fulfill(status=200,body=r.post_data,content_type='application/json')
    else:route.fulfill(status=200,body=json.dumps(db.get(k)),content_type='application/json')
def off(route):
    code=route.request.url.split('/product/')[1].split('.json')[0]
    body={'status':1,'product':{'product_name':'Vollmilch','brands':'Testmarke','quantity':'1 l','nutriscore_grade':'b','ingredients_text_de':'Milch'}} if code=='7610000000001' else {'status':0}
    route.fulfill(status=200,body=json.dumps(body),content_type='application/json')
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch();c=b.new_context(viewport={'width':390,'height':800})
    c.route('https://test-default-rtdb.firebaseio.com/**',fb);c.route('https://world.openfoodfacts.org/**',off)
    pg=c.new_page();pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{fbUrl:'https://test-default-rtdb.firebaseio.com'}}))");pg.reload()
    # Rückgängig
    for n in ['Brot','Käse']:pg.fill('#dn',n);pg.click('[data-a=add]')
    print('before',[i['name'] for i in st(pg)['items']])
    box=pg.locator('.card[data-swk=i]').first.bounding_box();y=box['y']+box['height']/2
    pg.mouse.move(box['x']+box['width']-20,y);pg.mouse.down();pg.mouse.move(box['x']+20,y,steps=8);pg.mouse.up();pg.wait_for_timeout(500)
    print('after swipe items',len(st(pg)['items']),'undo bar',pg.locator('.undo').count())
    pg.click('[data-a=undo]');print('after undo items',len(st(pg)['items']),'order',[i['name'] for i in st(pg)['items']])
    pg.mouse.move(box['x']+box['width']-20,y);pg.mouse.down();pg.mouse.move(box['x']+20,y,steps=8);pg.mouse.up();pg.wait_for_timeout(4300)
    print('undo gone after 4s',pg.locator('.undo').count(),'items',len(st(pg)['items']))
    # Zwischenkopien
    pg.reload();print('snapshots',pg.evaluate("JSON.parse(localStorage.getItem('sebu.bak')).length"))
    pg.click('#hamb');pg.click('.menu [data-v=settings]');pg.click('[data-a=sub][data-v=data]')
    print('restore buttons',pg.locator('[data-a=bakrest]').count())
    # Firebase-Sicherung
    pg.click('[data-chk=cloudBak]');pg.wait_for_timeout(500)
    code=st(pg)['set']['bakCode'];print('code len',len(code),'uploaded',len(db),'apiKey in backup', 'apiKey' in json.loads(list(db.values())[0]['j'])['set'] and json.loads(list(db.values())[0]['j'])['set']['apiKey']=='')
    pg.evaluate("var s=JSON.parse(localStorage.getItem('sebu.v1'));s.items=[];localStorage.setItem('sebu.v1',JSON.stringify(s))");pg.reload()
    pg.click('#hamb');pg.click('.menu [data-v=settings]');pg.click('[data-a=sub][data-v=data]')
    pg.fill('#bkc',code);pg.click('[data-a=bakget]');pg.wait_for_timeout(400);pg.click('[data-a=doimport]')
    print('restored items',len(st(pg)['items']))
    # Strichcode
    pg.click('#hamb');pg.click('.menu [data-v=list]')
    pg.click('[data-a=cam]');print('choice sheet',pg.locator('[data-a=scanopen]').count())
    pg.click('[data-a=scanopen]');pg.wait_for_timeout(300);print('scan sheet',pg.locator('#scn').count())
    pg.fill('#scn','7610000000001');pg.click('[data-a=scanlook]');pg.wait_for_timeout(400)
    print('found',pg.locator('.sheet b').first.inner_text(),'ns',pg.locator('.ns').inner_text())
    pg.screenshot(path='s13.png')
    pg.click('[data-a=scanadd]');pg.wait_for_timeout(200);print('added',[i['name'] for i in st(pg)['items']][-1:])
    pg.click('[data-a=cam]');pg.click('[data-a=scanopen]');pg.fill('#scn','7610000000099');pg.click('[data-a=scanlook]');pg.wait_for_timeout(400)
    print('not found',pg.locator('[data-a=scanhand]').count())
    b.close()
print(errs)
