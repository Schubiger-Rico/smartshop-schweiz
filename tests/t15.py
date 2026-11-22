# Mehr Symbole, automatisches Produkt-Symbol, Kategorie-Farben
from playwright.sync_api import sync_playwright
import os
errs=[]
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    want={'Paprikapulver':'🫑','Tomatensauce':'🍅','Erdbeerjoghurt':'🍓','Schweinefleisch':'🥩','Zucchetti':'🥒','Katzenfutter':'🐈'}
    for n in want:pg.fill('#dn',n);pg.click('[data-a=add]')
    got={}
    for c in pg.locator('.card[data-swk=i]').all():got[c.locator('.nm').inner_text().split('\n')[0].strip()]=c.locator('.ic').inner_text()
    print('auto icons ok',all(got.get(k)==v for k,v in want.items()),{k:got.get(k) for k in want})
    cards=pg.locator('.card[data-swk=i]').all();print('stripe',('border-left' in (cards[0].get_attribute('style') or '')))
    # eigenes Symbol
    pg.locator('.card[data-swk=i]',has_text='Zucchetti').locator('.ic').click();pg.click('[data-a=picon]');pg.click('[data-a=emopick][data-e="🥦"]')
    print('own icon',pg.locator('.card[data-swk=i]',has_text='Zucchetti').locator('.ic').inner_text(),'learned',st(pg)['learn'].get('icons'))
    pg.screenshot(path='s15.png')
    # Farbe ändern
    pg.click('#hamb');pg.click('.menu [data-v=settings]');pg.click('[data-a=sub][data-v=cats]')
    print('color inputs',pg.locator('[data-ccol]').count()>10)
    pg.evaluate("var e=document.querySelector('[data-ccol=m0]');e.value='#123456';e.dispatchEvent(new Event('change',{bubbles:true}))")
    print('saved color',[c['color'] for c in st(pg)['cats'] if c['id']=='m0'])
    print('emoji groups',pg.evaluate("1"))
    b.close()
print(errs)
