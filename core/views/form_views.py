from django.views.generic import TemplateView

from ..models import Criteria, Scale, JudgingRound, ScaleEntry, Team
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.contrib import messages
from ..utils.multiteams import MultientryPaperForm
from core.utils import csvutils


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
    
    
class PaperFormView(TemplateView):
    template_name = "core/paper_form_create.html"
    
    def post(self, request, *args, **kwargs):
        p = request.POST
        return HttpResponseRedirect(self.get_success_url())

    def get(self, request, *args, **kwargs):
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        
        crs = Criteria.objects.filter(judging_round=self.jr).all()
        columns = {}
        for cr in crs:
            scale_entries = list(ScaleEntry.objects.filter(scale=cr.scale).all().values_list('entry', flat=True))
            columns[cr.name] = scale_entries
            
        teams = list(Team.objects.filter(hackathon = self.jr.hackathon).all().values_list('name', flat=True))
        
        judge_id = 5
        qr_info = str(self.jr.pk)+";"+str(judge_id)
        form = MultientryPaperForm(qr_info,  columns, teams)

        form.save_template("C:\\temp\\template.xtmpl")
        form.save_as_pdf("C:\\temp\\form.pdf")
        
        csvutils.fs_csv_parse("C:\\temp\\scan\\results_20181210172459.csv")

        return super(PaperFormView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):        
        ret = super(PaperFormView, self).get_context_data(*args, **kwargs)
        return ret
    
        
    def get_success_url(self):
        return reverse("core:judging_round_detail", kwargs={'pk':self.kwargs['jround_id']})