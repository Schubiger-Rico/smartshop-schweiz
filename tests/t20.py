# Grössere Drehräder, Klick (gemockt) pro Schritt
from playwright.sync_api import sync_playwright
import os
errs=[]
MOCK="""window.__ticks=0;window.AudioContext=function(){this.state='running';this.currentTime=0;this.destination={};this.createOscillator=function(){window.__ticks++;return{type:'',frequency:{},connect:function(){},start:function(){},stop:function(){}}};this.createGain=function(){return{gain:{setValueAtTime:function(){},exponentialRampToValueAtTime:function(){}},connect:function(){}}};this.createBuffer=function(){return{}};this.createBufferSource=function(){return{connect:function(){},start:function(){}}};this.resume=function(){}};"""
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':390,'height':800});pg.on('pageerror',lambda e:errs.append(str(e)));pg.add_init_script(MOCK)
    pg.goto('file://'+os.getcwd()+'/index.html');pg.evaluate("localStorage.setItem('sebu.v1',JSON.stringify({ob:{done:true}}))");pg.reload()
    pg.click('[data-a=qty][data-id=draft]');pg.wait_for_timeout(600)
    h=pg.locator('#wq .o').first.bounding_box()['height'];print('row height >40',h>40,int(h))
    for k in range(1,4):pg.evaluate("var w=document.getElementById('wq');w.scrollTop=w.querySelector('.o').offsetHeight*%d"%k);pg.wait_for_timeout(80)
    pg.wait_for_timeout(300);print('ticks',pg.evaluate('window.__ticks'),'(3)','marked',pg.locator('#wq .o.on').inner_text(),'qm',pg.input_value('#qm'))
    pg.screenshot(path='s20.png')
    b.close()
print(errs)
