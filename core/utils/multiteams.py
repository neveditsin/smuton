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
    return(x+(sz/2), y+(sz/2))

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



class Table:
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


class Field:
    size = []
    textbox_sz = None
    label = ""
    font = None
    field_size = 0
    min_bw = 5
    bw = 0
    def __init__(self, font, field_size, label_pos, possible_values):
        self.field_size = field_size
        self.font = font
        self.textbox_sz = (max([font.getsize(val)[0] for val in possible_values]),
                           max([font.getsize(val)[1] for val in possible_values])) 
        self.label_pos = label_pos
        if (self.label_pos == 'L'):
            self.bw = math.ceil(self.textbox_sz[0]) + self.min_bw
        
    def do_draw(self, label, x, y):
        if (self.label_pos == 'L'):
            draw.text((x, y), label, font=self.font, fill=0)
            coords = circle(self.field_size, math.ceil(x+self.bw), y)
            return coords
    
    def get_size(self):
        if (self.label_pos == 'L'):
            return (math.ceil(self.textbox_sz[0])+self.bw+self.field_size, max(math.ceil(self.textbox_sz[1]),self.field_size))
        
    
corners(CORNERS,100,10)

t = Table(50,250,(WIDTH-50*2, HEIGHT-250-50),2,200,4, 300, 4)

font = ImageFont.truetype(font="arial.ttf", size=30)



def max_entries(avail, obj_sz, min_dist):
    return math.floor(avail/(obj_sz+min_dist))

def break_entries(n_entries, max_entries):
    if(n_entries > max_entries*2):
        raise ValueError('NCE001: Connot fit entries into cell with current configuration')
    d1 = math.floor(n_entries/2)
    d2 = n_entries - d1
    return(d2,d1)



def draw_entries(rc, cc, vertical, min_dist, margin, fld_sz, entries_list):
    sz = (rc[1] if vertical else cc[1])-margin*2
    if(vertical):
        f = Field(font, fld_sz, 'L', entries_list)
        obj_sz=f.get_size()[1]
    else:
        f = Field(font, fld_sz, 'L', entries_list)
        obj_sz=f.get_size()[0]  
        
    max_ent = max_entries(sz,obj_sz,min_dist)
    n_entries = len(entries_list)
    if(n_entries > max_ent):
        ent = break_entries(n_entries, max_ent)              
    else:
        ent = [n_entries]
                
    block = 0
    entry_idx = 0
    coords = []
    for nent in ent:    
        dist = math.floor(sz/nent - obj_sz)
        offset = ((rc[1] if vertical else cc[1])-((dist+obj_sz)*nent - dist))/2
        for i in range(0, nent):
            if (vertical):
                coords.append(f.do_draw(entries_list[entry_idx], cc[0]+margin+block, rc[0]+offset+(dist+obj_sz)*i))
            else:
                coords.append(f.do_draw(entries_list[entry_idx], cc[0]+offset+(dist+obj_sz)*i, rc[0]+margin+block))
            entry_idx+=1
    
        block+= math.floor((cc[1] if vertical else rc[1])/2)
    return coords
    



for rc in t.row_coords:
    for cc in t.col_coords:
        print(draw_entries(rc,cc,True, 15, 10, 30, ("1","2","3","4","1","2", "4","5","6")))
        


        
        


#draw.text((200, 500), "hello", font=font, fill=0)
#print(font.getsize("helloggggggggggggggggggggg"))



#print(circle(30, 300, 600))
print(mk_qrcode(8, CORNERS*2, CORNERS*2))

      
        




img.save("C:\\temp\\image.png", "PNG")


pdf = FPDF(unit = "pt", format = [WIDTH, HEIGHT])
pdf.add_page()
pdf.image("C:\\temp\\image.png", 0, 0)
pdf.output("C:\\temp\\form.pdf", "F")