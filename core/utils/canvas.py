from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import qrcode

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

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=8,
    border=4,
)

qr.add_data('{0:010d}'.format(1))
qr.make(fit=True)

qr_code = qr.make_image(fill_color="black", back_color="white")
print(qr_code.size)
img.paste(qr_code, (CORNERS*2,CORNERS*2))


corners(CORNERS,100,10)
font = ImageFont.truetype(font="arial.ttf", size=50)
draw.text((200, 500), "hello", font=font, fill=0)

print(font.getsize("helloggggggggggggggggggggg"))

print(circle(30, 300, 600))





img.save("C:\\temp\\image.png", "PNG")

from fpdf import FPDF
pdf = FPDF(unit = "pt", format = [WIDTH, HEIGHT])
pdf.add_page()
pdf.image("C:\\temp\\image.png", 0, 0)
pdf.output("C:\\temp\\form.pdf", "F")