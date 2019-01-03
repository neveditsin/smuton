from django.views.generic import TemplateView, FormView

from ..models import Criteria, Scale, JudgingRound, ScaleEntry, Team, Judge
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
    
    
    def post(self, request, *args, **kwargs):
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id'])
        wdir = os.path.join(settings.MEDIA_ROOT, str(self.jr.pk))
        dst_dir = os.path.join(wdir, "scanned") 
        if not os.path.exists(dst_dir):
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
                print(f)
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
            
            for ev in evaluators:
                qr_info = str(self.jr.pk)+";"+str(ev.pk)
                MultientryPaperForm(wdir,ev.name, str(ev.pk), qr_info, columns, teams)
            
            pdf_path = os.path.join(wdir, "form%d.pdf" % self.jr.pk)    
            MultientryPaperForm.make_pdf(wdir, pdf_path)
            
            if os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(pdf_path)
                    return response
            raise Http404  



        
        #csvutils.fs_csv_parse("C:\\temp\\scan\\results_20181210172459.csv")

        return super(PaperFormView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        ret = super(PaperFormView, self).get_context_data(*args, **kwargs)
        ret['jr'] = self.jr
        ret['file_form'] = UploadMultiFileForm()
        return ret
    
        
    def get_success_url(self):
        return reverse("core:paper_form", kwargs={'jround_id':self.kwargs['jround_id']})
    


    