
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import qrcode
import math 
from fpdf import FPDF 
import re
##testing only
import sys

sys.path.append('..')
##testing only END
from core.utils import template_creator
import glob
import os

class Table:
    row_coords = None
    col_coords = None   
    colname_boxes = None
    rowname_boxes = None    
    draw = None
    
    def __init__(self, draw, x,y, t_sz, line_wdth, header_height, nrow, row_header_width, ncol):
        self.row_coords = []
        self.col_coords = []
        self.colname_boxes = []
        self.rowname_boxes = []
        self.draw = draw
        self.draw_table(x,y, t_sz, line_wdth, header_height, nrow, row_header_width, ncol)

    @staticmethod
    def fit_count(header_height, t_sz, min_row_sz, nrow):
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
        else:
            return(1,nrow)
        
    def draw_table(self, x,y, t_sz, line_wdth, header_height, nrow, row_header_width, ncol):
        self.draw.rectangle(((x, y), (x+t_sz[0], y+t_sz[1])), outline=0, width=line_wdth)

        header_height = header_height
        self.draw.line(((x,y+header_height),(x+t_sz[0],y+header_height)), fill=0, width=line_wdth)        
        row_sz = math.floor((t_sz[1]-header_height)/nrow)
        
        self.row_coords.append((y+header_height,row_sz))

        self.rowname_boxes.append((x, y+header_height, row_header_width, header_height))
        for i in range(1, nrow):
            dy = math.floor(row_sz*i)
            _y = (y+header_height)+dy
            self.draw.line(((x,_y),(x+t_sz[0],_y)), fill=0, width=line_wdth)
            self.row_coords.append((_y,row_sz))
            self.rowname_boxes.append((x, _y, row_header_width, row_sz))
         

        self.draw.line(((x+row_header_width,y),(x+row_header_width, y+t_sz[1])), fill=0, width=line_wdth)
        
        col_sz = math.floor((t_sz[0]-row_header_width)/ncol)
        self.col_coords.append((x+row_header_width,col_sz))
        self.colname_boxes.append((x+row_header_width, y, col_sz, header_height))        
        for i in range(1, ncol):
            dx = math.floor(col_sz*i)
            _x = x+row_header_width+dx
            self.draw.line(((_x,y),(_x,y+t_sz[1])), fill=0, width=line_wdth)
            self.col_coords.append((_x,col_sz))
            self.colname_boxes.append((_x, y, col_sz, header_height))


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
    
#     @staticmethod
#     def the_static_method(x):
#         print(x)
            
    def square(self, sz, x, y):
        wdth = 3
        self.draw.rectangle(((x, y), (x+sz, y+sz)), outline=0, fill=1, width=wdth)
        return(x+(sz/2), y+(sz/2))
    
    def circle(self, sz, x, y):
        wdth = 3
        self.draw.ellipse((x, y, x+sz, y+sz), fill=1, outline = 0, width=wdth)
        return(x+(sz/2), y+(sz/2))
        
    def do_draw(self, label, x, y, isSquare):
        if (self.label_pos == 'L'):
            self.draw.text((x, y), label, font=self.font, fill=0)
            if isSquare:
                coords = self.square(self.field_size, math.ceil(x+self.bw), y)
            else:
                coords = self.circle(self.field_size, math.ceil(x+self.bw), y)
            return coords
    
    def get_size(self):
        if (self.label_pos == 'L'):
            return (math.ceil(self.textbox_sz[0])+self.bw+self.field_size, max(math.ceil(self.textbox_sz[1]),self.field_size))



class MultientryPaperFormPage:
    WIDTH = 3300 #hardcoded for now
    HEIGHT = 2550 #hardcoded for now
    CORNERS = 25 #hardcoded for now
    FIELD_SZ = 30
    FONT = "arial.ttf";
    img = Image.new('1', (WIDTH, HEIGHT), 1)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font=FONT, size=FIELD_SZ)
    t = None
    template = None
    DATA_SEPARATOR = '$__sep__$'   
    QR_FIELD = 'QR_INFO'
    T_SZ = (WIDTH-50*2, HEIGHT-250-50)
    
    def __init__(self,qr_info,columns,rownames, header_height, row_header_width, labels):
        ncol = len(columns)
        nrow = len(rownames)
        
        groups = []
        
        cornrs = self.corners(self.CORNERS,100,10)
        self.t = Table(self.draw, 50,250,self.T_SZ,2,header_height,nrow,row_header_width,ncol)
        qr_coords = self.mk_qrcode(qr_info, 8, self.CORNERS*2, self.CORNERS*2) 
        qr_group = template_creator.create_qr(self.QR_FIELD, 
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
                self.draw_text_in_box(header, self.font, self.t.colname_boxes[col_idx], 10) #header
                cc = self.t.col_coords[col_idx]                
                coords = self.draw_entries(rc,cc,False, 15, 10, 30,entries)
                resps = []        
                for c in coords:
                    resps.append(template_creator.create_resp(c[0], c[1][0], c[1][1]))
                                        
                groups.append(template_creator.create_group(header+self.DATA_SEPARATOR+row_val, resps))
                col_idx +=1
            row_idx+=1
        
        
        #name of event
        self.draw_text_in_box(labels[0], ImageFont.truetype(font=self.FONT, size=50), \
                              (qr_coords[2]+50, qr_coords[0], 2500, 100), 0)
        ##TODO round if >1
        self.draw_text_in_box("Evaluator: " + labels[1] + " (ID: " + labels[2] + ")",\
                              ImageFont.truetype(font=self.FONT, size=35), \
                              (qr_coords[2]+50, qr_coords[0]+100, 2500, 100), 0) 
        
        self.draw_text_in_box("Page 1 of 1",\
                              ImageFont.truetype(font=self.FONT, size=35), \
                              (qr_coords[2]+50, qr_coords[0]+135, 2500, 100), 0) 
                      
        self.template = template_creator.create_template(cornrs[0], cornrs[1], cornrs[2], cornrs[3],groups,math.floor(self.FIELD_SZ/2))


    
    def draw_text_in_box(self, text, font, box, margin):
      
        if(len(box) > 2):
            tsz = self.draw.textsize(text, font=font)
            box_width = box[2]-2*margin
            if(tsz[0] > box_width):
                #print(text)
                nlines = math.ceil(tsz[0]/box[2])
                approx_textlen = math.ceil(len(text)/nlines)
                start_idx = 0
                
                for ln in range(0,nlines):              
                    end_idx, carry = self.fit_text(text, start_idx, approx_textlen, font, box_width)                   
                    
                    
                    self.draw.text((box[0]+margin, box[1]+margin+ln*tsz[1]), \
                                   text[start_idx:end_idx] + ("-" if (ln < nlines-1 and carry) else ""),\
                                   font=font, fill=0)
                    start_idx = end_idx
            else:
                self.draw.text((box[0]+margin, box[1]+margin), text, font=font, fill=0)
        else:
            self.draw.text((box[0]+margin, box[1]+margin), text, font=font, fill=0)        
    
    def fit_text(self, text, start_idx, approx_textlen, font, box_width):
        end_idx = start_idx + approx_textlen;
        sz = self.draw.textsize(text[start_idx:end_idx], font=font) \
                + self.draw.textsize("-", font=font)
                
        while(sz[0] <= box_width):
            end_idx+=1
            if(end_idx >= len(text)):
                break
            sz = self.draw.textsize(text[start_idx:end_idx], font=font) \
                + self.draw.textsize("-", font=font)
       
        while(sz[0] - 5 > box_width):    
            end_idx-=1
            sz = self.draw.textsize(text[start_idx:end_idx], font=font) \
                + self.draw.textsize("-", font=font)
        
        #carry or not?
        carry = True
        last = text[start_idx:end_idx].split(" ")[-1]
        if len(last) < 2:
            end_idx-= 1
            carry = False
            
        if len(last) == 2 and not re.match("A-Za-z", last[0]):
            end_idx-= 2
            carry = False 
        
        
        return (end_idx, carry)
       

    def get_template(self):
        return self.template
    
    def save_template(self, path):
        text_file = open(path, "w")
        text_file.write(self.get_template())
        text_file.close()

              
    def save_as_image(self,path): #"C:\\temp\\image.png"
        self.img.save(path, "PNG")
    
 
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
    
    #currently only max_entries*2 supported. Can be done for more entries later if necessary
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
            f = Field(self.font, self.draw, fld_sz, 'L', entries_list)
            obj_sz=f.get_size()[0]  
            
        max_ent = self.max_entries(sz,obj_sz,min_dist)
        n_entries = len(entries_list)
        if(n_entries > max_ent):
            ent = self.__break_entries(n_entries, max_ent)              
        else:
            ent = [n_entries]
            
        
        centering = math.floor((cc[1] if vertical else rc[1])/(len(ent)+1))          
        block = centering
        entry_idx = 0
        coords = []
        for nent in ent:    
            dist = math.floor(sz/nent - obj_sz)
            offset = ((rc[1] if vertical else cc[1])-((dist+obj_sz)*nent - dist))/2
            for i in range(0, nent):
                if (vertical):
                    coords.append((entries_list[entry_idx], f.do_draw(entries_list[entry_idx], cc[0]+margin+block, rc[0]+offset+(dist+obj_sz)*i, False)))
                else:
                    coords.append((entries_list[entry_idx], f.do_draw(entries_list[entry_idx], cc[0]+offset+(dist+obj_sz)*i, rc[0]+margin+block, False)))
                entry_idx+=1
        
            block+= centering
        return coords



class MultientryPaperForm:
    npages = 1
    
    def __init__(self, wd, title, ev_name, ev_id, fileprefix, qr_info, columns, rownames):
        #todo: automatically
        header_height = 200
        row_header_width = 300
        min_row_sz = 120
        self.wd = wd

        self.npages, max_nrows = Table.fit_count(header_height, MultientryPaperFormPage.T_SZ, min_row_sz, len(rownames))
        if self.npages > 1:
            raise Exception("Not implemented for multiple pages")
            #break the page by max_nrows
        
        for i in range(0,self.npages):
            rows_lower = i*max_nrows
            rows_upper = min(i*max_nrows+max_nrows,len(rownames))
            page = MultientryPaperFormPage(qr_info,columns,rownames[rows_lower:rows_upper], \
                                           header_height, row_header_width, [title, ev_name, ev_id, i+1])
            page.save_template(os.path.join(self.wd, "template%d.xtmpl" % i) )
            page.save_as_image(os.path.join(self.wd, fileprefix + "_img%d.png" % i))
            
        #self.make_pdf(self.wd + "form.pdf")
    
    @staticmethod
    def make_pdf(wd, outpath):   
            pdf = FPDF(unit = "pt", format = [MultientryPaperFormPage.WIDTH, MultientryPaperFormPage.HEIGHT])
            for img in glob.glob(os.path.join(wd, '*_img*.png')):
                #print(img)
                pdf.add_page()
                pdf.image(img, 0, 0)
            pdf.output(outpath, "F") #"C:\\temp\\form.pdf"

#data '{0:010d}'.format(1)

