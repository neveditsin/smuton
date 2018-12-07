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



class table:
    row_coords = []
    col_coords = []
    
    def __init__(self, x,y, t_sz, line_wdth, header_height, nrow, row_header_height, ncol):
        self.draw_table(x,y, t_sz, line_wdth, header_height, nrow, row_header_height, ncol)
        
    
    def fit_count(self, header_height, t_sz, min_row_sz, nrow):
        row_sz = (t_sz[1]-header_height)/nrow
        if row_sz < min_row_sz:
            row_sz = min_row_sz
            #recalculate count
            count_fit = math.floor((t_sz[1]-header_height)/min_row_sz)       
            #recalculate row_size
            row_sz = (t_sz[1]-header_height)/count_fit
            #pages_count
            pg_count = math.ceil(nrow/count_fit)
            return(pg_count,count_fit)
        
    def draw_table(self, x,y, t_sz, line_wdth, header_height, nrow, row_header_height, ncol):
        draw.rectangle(((x, y), (x+t_sz[0], y+t_sz[1])), outline=0, width=line_wdth)
        #horizontal
        #header
        header_height = header_height
        draw.line(((x,y+header_height),(WIDTH-x,y+header_height)), fill=0, width=line_wdth)
        
        row_sz = math.floor((t_sz[1]-header_height)/nrow)
        self.row_coords.append((y+header_height,row_sz))
        for i in range(1, nrow):
            dy = math.floor(row_sz*i)
            _y = (y+header_height)+dy
            draw.line(((x,_y),(WIDTH-x,_y)), fill=0, width=line_wdth)
            self.row_coords.append((_y,row_sz))
         
        #vertical
        #row_lables
        draw.line(((x+row_header_height,y),(x+row_header_height, y+t_sz[1])), fill=0, width=line_wdth)
        
        col_sz = math.floor((t_sz[0]-row_header_height)/ncol)
        self.col_coords.append((x+row_header_height,col_sz))
        for i in range(1, ncol):
            dx = math.floor(col_sz*i)
            _x = x+row_header_height+dx
            draw.line(((_x,y),(_x,y+t_sz[1])), fill=0, width=line_wdth)
            self.col_coords.append((_x,col_sz))

    
corners(CORNERS,100,10)

t = table(50,250,(WIDTH-50*2, HEIGHT-250-50),2,200,8, 300, 10)

n_entries = 5
obj_sz = 30
margin = 10
min_dist = 15


def max_entries(avail, obj_sz, min_dist):
    return math.floor(avail/(obj_sz+min_dist))

def break_entries(n_entries, max_entries):
    if(n_entries > max_entries*2):
        raise ValueError('NCE001: Connot fit entries into cell with current configuration')
    d1 = math.floor(n_entries/2)
    d2 = n_entries - d1
    return(d2,d1)


for rc in t.row_coords:
    for cc in t.col_coords:
        v_sz = rc[1]-margin*2
        max_ent = max_entries(v_sz,obj_sz,min_dist)
        if(n_entries > max_ent):
            ent = break_entries(n_entries, max_ent)              
        else:
            ent = [n_entries]
                    
        block = 0
        for v_entries in ent:    
            dist = v_sz/v_entries - obj_sz
            v_offset = (rc[1]-((dist+obj_sz)*v_entries - dist))/2
            #d_count = v_sz/(obj_sz+dist)
            for i in range(0, v_entries):            
                circle(obj_sz,cc[0]+margin+block, rc[0]+v_offset+(dist+obj_sz)*i)
        
            block+= math.floor(cc[1]/2)
        
        
        

font = ImageFont.truetype(font="arial.ttf", size=50)
#draw.text((200, 500), "hello", font=font, fill=0)
#print(font.getsize("helloggggggggggggggggggggg"))



#print(circle(30, 300, 600))
print(mk_qrcode(8, CORNERS*2, CORNERS*2))

      
        




img.save("C:\\temp\\image.png", "PNG")


pdf = FPDF(unit = "pt", format = [WIDTH, HEIGHT])
pdf.add_page()
pdf.image("C:\\temp\\image.png", 0, 0)
pdf.output("C:\\temp\\form.pdf", "F")