from django.views.generic import TemplateView, FormView

from ..models import Criteria, Scale, JudgingRound, ScaleEntry, Team, Judge, JudgeResponse
from ..forms import UploadMultiFileForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.contrib import messages
from ..utils.multiteams import MultientryPaperForm
from core.utils import csvutils
from django.conf import settings 
import os
from django.http import HttpResponse, Http404
from django.core.files.base import ContentFile 

from subprocess import check_call
import shutil
from os.path import isfile, join
import re
import pandas as pd
import glob
from multiprocessing.dummy import Pool as ThreadPool 

class SumbitFormView(TemplateView):
    template_name = "core/form_create.html"
    
    def post(self, request, *args, **kwargs):
        p = request.POST
        i = 1 #start from name1, scale1
        jr = JudgingRound.objects.get(pk=self.kwargs['jround_id'])
        while 'name'+str(i) in p:
            try:  
                name = p['name'+str(i)]
                scale = p['scale'+str(i)] 
                Criteria.objects.create(
                    name = name,
                    scale = Scale.objects.get(pk=scale),
                    judging_round = jr
                    )
                i+=1
            except IntegrityError:
                ##TODO need to properly handle it
                messages.error(request, "Fatal error: criteria  '" + name + "' alredy exists")
                return HttpResponseRedirect(request.path)
        
        return HttpResponseRedirect(self.get_success_url())

    
    def get_context_data(self, *args, **kwargs):        
        ret = super(SumbitFormView, self).get_context_data(*args, **kwargs)
        ret['scale'] = Scale.objects.all()
        return ret
    
        
    def get_success_url(self):
        return reverse("core:judging_round_detail", kwargs={'pk':self.kwargs['jround_id']})
    

class PaperFormView(FormView):
    template_name = "core/paper_form_create.html"
    form_class = UploadMultiFileForm
    SCAN_DIR = 'scanned'
    
    def post(self, request, *args, **kwargs):
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id'])
        wdir = os.path.join(settings.MEDIA_ROOT, str(self.jr.pk))
        dst_dir = os.path.join(wdir, self.SCAN_DIR)
        
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)
        
        os.makedirs(dst_dir)
        
                
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                out = open(os.path.join(dst_dir, str(f)), 'wb+')
                content = ContentFile(f.read())
                for chunk in content.chunks():
                    out.write(chunk)
                out.close()               
                
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        
        if request.GET.get('download', 'no') == "yes":
            crs = Criteria.objects.filter(judging_round=self.jr).all()
            columns = {}
            for cr in crs:
                scale_entries = list(ScaleEntry.objects.filter(scale=cr.scale).all().values_list('entry', flat=True))
                columns[cr.name] = scale_entries
                
            teams = list(Team.objects.filter(hackathon = self.jr.hackathon).all().values_list('name', flat=True))
            
    
    
            
            wdir = os.path.join(settings.MEDIA_ROOT, str(self.jr.pk))
            print(wdir)
            if not os.path.exists(wdir):
                os.makedirs(wdir)
                
            evaluators = Judge.objects.filter(hackathon=self.jr.hackathon).all()
            
      
            #cleanup first    
            current_files = os.path.join(wdir, "*.png")
            r = glob.glob(current_files)
            for i in r:
                os.remove(i)
            

            #pool = ThreadPool(8) 
            
            def gen_form(ev):
                qr_info = str(ev.pk)
                MultientryPaperForm(wdir, self.jr.hackathon.name, ev.name, str(ev.pk), str(ev.pk), qr_info, columns, teams)
            
            #pool.map(gen_form, evaluators)          
                       
            for ev in evaluators:
                gen_form(ev)
            
            #pool.close() 
            #pool.join() 
            
            pdf_path = os.path.join(wdir, "form%d.pdf" % self.jr.pk)    
            MultientryPaperForm.make_pdf(wdir, pdf_path)
            
            if os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(pdf_path)
                    return response
            raise Http404  



        
        

        return super(PaperFormView, self).get(request, *args, **kwargs)
    
    
    def get_context_data(self, *args, **kwargs):
        ret = super(PaperFormView, self).get_context_data(*args, **kwargs)
        ret['jr'] = self.jr
        ret['file_form'] = UploadMultiFileForm()
        img_path = os.path.join(settings.MEDIA_ROOT, str(self.jr.pk), self.SCAN_DIR)
        if not os.path.exists(img_path):
            os.makedirs(img_path)

        lst = [f for f in os.listdir(img_path) if (isfile(join(img_path, f)) and (bool(re.search('jpg', f))) or bool(re.search('png', f))) ]
        ret['files_list'] = lst
        return ret
    
        
    def get_success_url(self):
        return reverse("core:paper_form", kwargs={'jround_id':self.kwargs['jround_id']})
    
    
    
class PaperFormResultsPreview(TemplateView):
    template_name = "core/paper_form_res_preview.html"
     

    def get(self, request, *args, **kwargs):
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        
        wdir = os.path.join(settings.MEDIA_ROOT, str(self.jr.pk))
        img_path = os.path.join(settings.MEDIA_ROOT, str(self.jr.pk), PaperFormView.SCAN_DIR)        
        
        
        #remove old results files
        for f in os.listdir(img_path):
            if re.search("results_.*.csv", f):
                os.remove(os.path.join(img_path, f))
        

        if (check_call(["java", "-jar", settings.FS_PATH, os.path.join(wdir, "template0.xtmpl"), img_path]) == 0):
            for f in os.listdir(img_path):
                if re.search("results_.*.csv", f):
                    res_path = join(img_path, f)
                    self.jtcm = csvutils.fs_csv_parse(res_path, self.jr)            
        
        if request.GET.get('csv', 'no') == "yes": 
            #assume that results.csv file with parsed responses is already here
            df = self.get_context_data()['pt']
                    
            csv_path = os.path.join(settings.MEDIA_ROOT, str(self.jr.pk),\
                                    "results_csv_" + str(self.jr.pk) + ".csv"  )
            
            df.to_csv(path_or_buf=csv_path, index=False)
            if os.path.exists(csv_path):
                with open(csv_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(csv_path)
                    return response
        
        
        if request.GET.get('upload', 'no') == "yes":            
            for rsp in self.jtcm:           
                JudgeResponse.objects.update_or_create(
                            round = self.jr,
                            team = rsp[1],
                            judge = rsp[0],
                            criterion = rsp[2],
                            mark = rsp[3],
                            )                            
            return HttpResponseRedirect(reverse("core:judging_round_detail", kwargs={'pk':self.jr.pk}))
        


        return super(PaperFormResultsPreview, self).get(request, *args, **kwargs)
    
    
    def get_context_data(self, *args, **kwargs):
        ret = super(PaperFormResultsPreview, self).get_context_data(*args, **kwargs)
        ret['jr'] = self.jr
        
        if not self.jtcm:
            return ret           
        
        df = pd.DataFrame.from_records(self.jtcm)
        df.columns = ['judge_name', 'team_name', 'criteria', 'mark']
        df['judge_name'] = df['judge_name'].astype('str') 
        df['team_name'] = df['team_name'].astype('str') 
        df['criteria'] = df['criteria'].astype('str')     

        df['mark'] = df['mark'].astype('str')
        
        pt = pd.DataFrame(df.pivot_table(index=['judge_name','team_name'], 
                                 columns='criteria', 
                                 values='mark', 
                                 aggfunc='first').to_records())

        ret['pt'] = pt;
        ret['jtcm'] = pt.to_html();
        
        
        
        
        return ret
    
        
    def get_success_url(self):
        return reverse("core:paper_form", kwargs={'jround_id':self.kwargs['jround_id']})
    


    