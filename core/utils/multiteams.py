from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import qrcode
from fpdf import FPDF
import math 

WIDTH = 3300
HEIGHT = 2550
CORNERS = 25
img = Image.new('1', (WIDTH, HEIGHT), 1)
draw = ImageDraw.Draw(img)

def corners(margin, size, width):
    draw.rectangle([(margin, margin), (WIDTH-margin, HEIGHT-margin)], outline = 0, width=width)
    draw.rectangle([(margin+size, 0), (WIDTH-margin-size, HEIGHT)], outline=1, fill=1)
    draw.rectangle([(0, margin+size), (WIDTH, HEIGHT-margin-size)], outline=1, fill=1)
    
def square(sz, x, y):
    wdth = 3
    draw.rectangle(((x, y), (x+sz, y+sz)), outline=0, fill=1, width=wdth)
    return(x+sz/2, y+sz/2)

def circle(sz, x, y):
    wdth = 3
    draw.ellipse((x, y, x+sz, y+sz), fill=1, outline = 0, width=wdth)
    return(x+sz/2, y+sz/2)

def mk_qrcode(boxsz, x,y):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=boxsz,
        border=0)
    qr.add_data('{0:010d}'.format(1))
    qr.make(fit=True)  
    qr_code = qr.make_image(fill_color="black", back_color="white")
    img.paste(qr_code, (x,y))
    return(x,y,qr_code.size[0]+x,qr_code.size[1]+y)
      


corners(CORNERS,100,10)
font = ImageFont.truetype(font="arial.ttf", size=50)
#draw.text((200, 500), "hello", font=font, fill=0)
#print(font.getsize("helloggggggggggggggggggggg"))



#print(circle(30, 300, 600))
print(mk_qrcode(8, CORNERS*2, CORNERS*2))

x = 50
y = 250
t_sz = (WIDTH-x*2, HEIGHT-y-50) 
draw.rectangle(((x, y), (x+t_sz[0], y+t_sz[1])), outline=0, width=2)

#horizontal
#header
header_height = 150
draw.line(((x,y+header_height),(WIDTH-x,y+header_height)), fill=0, width=2)
#rows
min_row_sz = 200
row_count = 5
row_sz = (t_sz[1]-header_height)/row_count
if row_sz < min_row_sz:
    print("size is too small. using minimal size")
    row_sz = min_row_sz
    #recalculate count
    count_fit = math.floor((t_sz[1]-header_height)/min_row_sz)
    print(count_fit)
    count_fit = 10
for i in range(1, row_count):
    dy = math.floor(row_sz*i)
    draw.line(((x,(y+header_height)+dy),(WIDTH-x,(y+header_height)+dy)), fill=0, width=2)


img.save("C:\\temp\\image.png", "PNG")


pdf = FPDF(unit = "pt", format = [WIDTH, HEIGHT])
pdf.add_page()
pdf.image("C:\\temp\\image.png", 0, 0)
pdf.output("C:\\temp\\form.pdf", "F")