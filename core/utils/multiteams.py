
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import qrcode
import math 
from fpdf import FPDF 

##testing only
import sys
sys.path.append('..')
##testing only END
from core.utils import template_creator


class Table:
    row_coords = None
    col_coords = None   
    colname_boxes = None
    rowname_boxes = None    
    draw = None
    
    def __init__(self, draw, x,y, t_sz, line_wdth, header_height, nrow, row_header_height, ncol):
        self.row_coords = []
        self.col_coords = []
        self.colname_boxes = []
        self.rowname_boxes = []
        self.draw = draw
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
        
    def draw_table(self, x,y, t_sz, line_wdth, header_height, nrow, row_header_width, ncol):
        self.draw.rectangle(((x, y), (x+t_sz[0], y+t_sz[1])), outline=0, width=line_wdth)

        header_height = header_height
        self.draw.line(((x,y+header_height),(x+t_sz[0],y+header_height)), fill=0, width=line_wdth)        
        row_sz = math.floor((t_sz[1]-header_height)/nrow)
        
        self.row_coords.append((y+header_height,row_sz))

        self.rowname_boxes.append((x, y+header_height, x+row_header_width, y+header_height+row_sz))
        for i in range(1, nrow):
            dy = math.floor(row_sz*i)
            _y = (y+header_height)+dy
            self.draw.line(((x,_y),(x+t_sz[0],_y)), fill=0, width=line_wdth)
            self.row_coords.append((_y,row_sz))
            self.rowname_boxes.append((x, _y, x+row_header_width, _y+row_sz))
         

        self.draw.line(((x+row_header_width,y),(x+row_header_width, y+t_sz[1])), fill=0, width=line_wdth)
        
        col_sz = math.floor((t_sz[0]-row_header_width)/ncol)
        self.col_coords.append((x+row_header_width,col_sz))
        self.colname_boxes.append((x+row_header_width, y, x+row_header_width+col_sz, y+header_height))        
        for i in range(1, ncol):
            dx = math.floor(col_sz*i)
            _x = x+row_header_width+dx
            self.draw.line(((_x,y),(_x,y+t_sz[1])), fill=0, width=line_wdth)
            self.col_coords.append((_x,col_sz))
            self.colname_boxes.append((_x, y, _x+col_sz, y+header_height))


class Field:
    size = []
    textbox_sz = None
    label = ""
    font = None
    field_size = 0
    min_bw = 5
    bw = 0
    def __init__(self, font, draw, field_size, label_pos, possible_values):
        self.draw = draw
        self.field_size = field_size
        self.font = font
        self.textbox_sz = (max([font.getsize(val)[0] for val in possible_values]),
                           max([font.getsize(val)[1] for val in possible_values])) 
        self.label_pos = label_pos
        if (self.label_pos == 'L'):
            self.bw = math.ceil(self.textbox_sz[0]) + self.min_bw
            
    def square(self, sz, x, y):
        wdth = 3
        self.draw.rectangle(((x, y), (x+sz, y+sz)), outline=0, fill=1, width=wdth)
        return(x+sz/2, y+sz/2)
    
    def circle(self, sz, x, y):
        wdth = 3
        self.draw.ellipse((x, y, x+sz, y+sz), fill=1, outline = 0, width=wdth)
        return(x+(sz/2), y+(sz/2))
        
    def do_draw(self, label, x, y):
        if (self.label_pos == 'L'):
            self.draw.text((x, y), label, font=self.font, fill=0)
            coords = self.circle(self.field_size, math.ceil(x+self.bw), y)
            return coords
    
    def get_size(self):
        if (self.label_pos == 'L'):
            return (math.ceil(self.textbox_sz[0])+self.bw+self.field_size, max(math.ceil(self.textbox_sz[1]),self.field_size))



class MultientryPaperForm:
    WIDTH = 3300 #hardcoded for now
    HEIGHT = 2550 #hardcoded for now
    CORNERS = 25 #hardcoded for now
    FIELD_SZ = 30
    img = Image.new('1', (WIDTH, HEIGHT), 1)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font="arial.ttf", size=FIELD_SZ)
    t = None
    template = None
    DATA_SEPARATOR = '$__sep__$'
   
    
    def __init__(self,qr_info,columns,rownames):
        ncol = len(columns)
        nrow = len(rownames)
        
        groups = []
        
        cornrs = self.corners(self.CORNERS,100,10)
        self.t = Table(self.draw, 50,250,(self.WIDTH-50*2, self.HEIGHT-250-50),2,200,nrow,300,ncol)
        qr_coords = self.mk_qrcode(qr_info, 8, self.CORNERS*2, self.CORNERS*2) 
        qr_group = template_creator.create_qr("Evaluator", 
                                    (qr_coords[0]             , qr_coords[1]),
                                    (qr_coords[0]+qr_coords[2], qr_coords[1]),
                                    (qr_coords[0]             , qr_coords[1]+qr_coords[3]),
                                    (qr_coords[0]+qr_coords[2], qr_coords[1]+qr_coords[3]))
        groups.append(qr_group)
        

        row_idx = 0
        for rc in self.t.row_coords:
            row_val = rownames[row_idx]
            self.draw_text_in_box(row_val, self.font, self.t.rowname_boxes[row_idx], 10)
            col_idx = 0
            for header, entries in columns.items():
                self.draw_text_in_box(header, self.font, self.t.colname_boxes[col_idx], 10)
                cc = self.t.col_coords[col_idx]                
                coords = self.draw_entries(rc,cc,True, 15, 10, 30,entries)
                resps = []        
                for c in coords:
                    resps.append(template_creator.create_resp(c[0], c[1][0], c[1][1]))
                                        
                groups.append(template_creator.create_group(header+self.DATA_SEPARATOR+row_val, resps))
                col_idx +=1
            row_idx+=1

        self.template = template_creator.create_template(cornrs[0], cornrs[1], cornrs[2], cornrs[3],groups,self.FIELD_SZ)

    def draw_text_in_box(self, text, font, box, margin):
        #TODO FIT
        self.draw.text((box[0]+margin, box[1]+margin), text, font=font, fill=0)

    def get_template(self):
        return self.template
    
    def save_template(self, path):
        text_file = open(path, "w")
        text_file.write(self.get_template())
        text_file.close()

              
    def __save_as_image(self,path): #"C:\\temp\\image.png"
        self.img.save(path, "PNG")
    
    def save_as_pdf(self,path):
            self.__save_as_image("C:\\temp\\image.png")          
            pdf = FPDF(unit = "pt", format = [self.WIDTH, self.HEIGHT])
            pdf.add_page()
            pdf.image("C:\\temp\\image.png", 0, 0)
            pdf.output(path, "F") #"C:\\temp\\form.pdf"
    
    def corners(self, margin, size, width):
        self.draw.rectangle([(margin, margin), (self.WIDTH-margin, self.HEIGHT-margin)], outline = 0, width=width)
        self.draw.rectangle([(margin+size, 0), (self.WIDTH-margin-size, self.HEIGHT)], outline=1, fill=1)
        self.draw.rectangle([(0, margin+size), (self.WIDTH, self.HEIGHT-margin-size)], outline=1, fill=1)
        return ((margin, margin), (self.WIDTH-margin, margin), 
                (margin, self.HEIGHT-margin), (self.WIDTH-margin, self.HEIGHT-margin),)
        
    
    def mk_qrcode(self,data,boxsz, x,y):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=boxsz,
            border=0)
        qr.add_data(data)
        qr.make(fit=True)  
        qr_code = qr.make_image(fill_color="black", back_color="white")
        self.img.paste(qr_code, (x,y))        
        return (x,y,qr_code.size[0]+x,qr_code.size[1]+y)
      
    
    def max_entries(self, avail, obj_sz, min_dist):
        return math.floor(avail/(obj_sz+min_dist))
    
    def __break_entries(self, n_entries, max_entries):
        if(n_entries > max_entries*2):
            raise ValueError('NCE001: Connot fit entries into cell with current configuration')
        d1 = math.floor(n_entries/2)
        d2 = n_entries - d1
        return(d2,d1)
         
  
    def draw_entries(self, rc, cc, vertical, min_dist, margin, fld_sz, entries_list):
        sz = (rc[1] if vertical else cc[1])-margin*2
        if(vertical):
            f = Field(self.font, self.draw, fld_sz, 'L', entries_list)
            obj_sz=f.get_size()[1]
        else:
            f = Field(self.font, fld_sz, 'L', entries_list)
            obj_sz=f.get_size()[0]  
            
        max_ent = self.max_entries(sz,obj_sz,min_dist)
        n_entries = len(entries_list)
        if(n_entries > max_ent):
            ent = self.__break_entries(n_entries, max_ent)              
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
                    coords.append((entries_list[entry_idx], f.do_draw(entries_list[entry_idx], cc[0]+margin+block, rc[0]+offset+(dist+obj_sz)*i)))
                else:
                    coords.append((entries_list[entry_idx], f.do_draw(entries_list[entry_idx], cc[0]+offset+(dist+obj_sz)*i, rc[0]+margin+block)))
                entry_idx+=1
        
            block+= math.floor((cc[1] if vertical else rc[1])/2)
        return coords


#data '{0:010d}'.format(1)

