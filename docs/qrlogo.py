import qrcode,sys
from PIL import Image,ImageDraw,ImageFont
def make(out):
    q=qrcode.QRCode(border=2,box_size=12,error_correction=qrcode.constants.ERROR_CORRECT_H);q.add_data('https://schubiger-rico.github.io/smartshop-schweiz/');q.make(fit=True)
    img=q.make_image(fill_color='#0a2a00',back_color='white').convert('RGB');W,H=img.size
    bw,bh=int(W*.38),int(H*.17);x0,y0=(W-bw)//2,(H-bh)//2
    d=ImageDraw.Draw(img);d.rounded_rectangle([x0,y0,x0+bw,y0+bh],radius=int(bh*.28),fill='#0f1815',outline='#39FF14',width=4)
    f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',int(bh*.6))
    t=Image.new('RGBA',(bw*2,bh*2),(0,0,0,0));td=ImageDraw.Draw(t)
    td.text((bh*.4,bh*.3),'sEBU',font=f,fill='#39FF14',stroke_width=3,stroke_fill='#0a5c00')
    t=t.transform(t.size,Image.AFFINE,(1,0.22,-bh*0.1,0,1,0),resample=Image.BICUBIC);t=t.crop(t.getbbox())
    img.paste(t,((W-t.width)//2,(H-t.height)//2),t);img.save(out);return img
make(sys.argv[1])
