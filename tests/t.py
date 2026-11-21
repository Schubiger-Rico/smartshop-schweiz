from playwright.sync_api import sync_playwright
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800})
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.on('console',lambda m:errs.append(m.text) if m.type=='error' and 'net::' not in m.text else None)
    pg.goto('file://'+__import__('os').getcwd()+'/index.html');pg.wait_for_timeout(500)
    pg.click('[data-a=onname][data-skip]');pg.click('[data-a=onsize]');pg.click('[data-a=ontour][data-v="0"]');pg.click('[data-a=onset][data-v="0"]')
    pg.fill('#dn','Rüebli');pg.click('[data-a=qty]');pg.fill('#qm','2');pg.click('[data-a=qtyok]');pg.click('[data-a=add]')
    pg.fill('#dn','Zopfmehl');pg.click('[data-a=add]')
    pg.fill('#dn','Xyzzy');pg.click('[data-a=add]')
    print('ask' , pg.locator('[data-a=askskip]').count())
    pg.click('[data-a=askskip]')
    print('cards',pg.locator('.card[data-swk=i]').count())
    pg.click('.card [data-a=check]');print('cards',pg.locator('.card[data-swk=i]').count(),'recent',pg.locator('.card.done').count())
    pg.click('.card .fire');pg.click('.card [data-a=fav]')
    # hold fire
    pg.hover('.card .fire');pg.mouse.down();pg.wait_for_timeout(2200);pg.mouse.up();print('sheet',pg.locator('.sheet').count());pg.screenshot(path='s1.png')
    pg.click('[data-a=shclose] [data-a=shclose]') if False else pg.mouse.click(200,20)
    for v in ['favs','deals','ideas','settings','advice','events','stamm','kipro','test']:
        pg.click('#hamb')
        if v in('advice','events','stamm','kipro','test'):pg.click('[data-a=more]')
        pg.click('[data-a=nav][data-v=%s]'%v);pg.wait_for_timeout(100)
    pg.click('#hamb');pg.click('[data-a=nav][data-v=settings]')
    for s in ['profil','look','lang','cats','favs','gps','stores','learn','price','ai','plan','tour','data']:
        pg.click('[data-a=sub][data-v=%s]'%s);pg.click('[data-a=sub][data-v=main]')
    pg.click('[data-a=sub][data-v=cats]');pg.click('[data-a=mainadd]');pg.click('[data-a=up] >> nth=3');pg.screenshot(path='s2.png')
    pg.click('#hamb');pg.click('[data-a=nav][data-v=list]')
    pg.click('#hamb');pg.click('[data-a=nav][data-v=settings]');pg.click('[data-a=sub][data-v=tour]');pg.click('[data-a=tour][data-v=app]')
    for i in range(150):
        if pg.locator('.tc').count()==0:break
        try:
            if pg.locator('[data-a=tnext]').count():pg.click('[data-a=tnext]')
            else:
                if pg.locator('#dn').count() and pg.locator('.hl #dn').count():
                    pg.fill('#dn','Milch');pg.click('[data-a=add]')
                else: pg.click('.hl')
        except Exception as e: errs.append('tour '+str(i)+str(e)[:100]);print(pg.inner_text('.tc'));pg.screenshot(path='s5.png');break
    print(pg.inner_text('.tc') if pg.locator('.tc').count() else 'none', pg.locator('.hl').count())
    print('tour done', pg.locator('.tc').count()==0)
    # swipe
    print(pg.evaluate("localStorage.getItem('sebu.v1').length"))
    b.close()
print('ERRS',errs)
