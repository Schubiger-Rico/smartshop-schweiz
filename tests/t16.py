# Kopfzeile aufgeräumt, Sprache (Spracherkennung gemockt), Öle
from playwright.sync_api import sync_playwright
import os
errs=[]
MOCK="""window.webkitSpeechRecognition=function(){var me=this;this.start=function(){setTimeout(function(){me.onresult({results:[[{transcript:'Milch, Brot und zwei Kilo Äpfel sowie 3 Dosen Mais'}]]});me.onend&&me.onend()},50)};this.abort=function(){}};window.SpeechRecognition=window.webkitSpeechRecognition;"""
def st(pg):return pg.evaluate("JSON.parse(localStorage.getItem('sebu.v1'))")
with sync_playwright() as p:
    b=p.chromium.launch()
    for fs in [18,24]:
        pg=b.new_page(viewport={'width':390,'height':700});pg.on('pageerror',lambda e:errs.append(str(e)));pg.add_init_script(MOCK)
        pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true},set:{fs:%d}}))"%fs);pg.reload()
        bar=pg.locator('.topbar').bounding_box();print('fs',fs,'topbar one line',bar['height']<60,'start text',pg.inner_text('#shopbtn'))
        w=pg.locator('#dn').bounding_box()['width'];print(' input width',int(w))
        pg.screenshot(path='s16_%d.png'%fs)
        if fs==18:
            pg.click('[data-a=voice]');pg.wait_for_timeout(300)
            print(' heard rows',pg.locator('.sheet .row').count(),pg.locator('.sheet .row').all_inner_texts())
            pg.click('[data-a=voiceadd]');print(' items',[(i['name'],i['qty'],i['unit']) for i in st(pg)['items']])
            pg.fill('#dn','Rapsöl');pg.click('[data-a=add]');print(' oil icon',pg.locator('.card[data-swk=i]',has_text='Rapsöl').locator('.ic').inner_text())
        pg.close()
    b.close()
print(errs)
