from django.views.generic import TemplateView

from ..models import Criteria, Scale, JudgingRound
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.contrib import messages
from ..utils.multiteams import MultientryPaperForm


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
        
        form = MultientryPaperForm("Nik Nev",  {"header1": ("AA","2","3"),
                                      "header2": ("11","12","13"),
                                      "header3": ("a","b","c"),
                                      "header4": ("yes","no")
                                      }, 
                                      ("team1", "team2", "team3", "team4"))

        form.save_template("C:\\temp\\template.xtmpl")
        form.save_as_pdf("C:\\temp\\form.pdf")

        return super(PaperFormView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):        
        ret = super(PaperFormView, self).get_context_data(*args, **kwargs)
        return ret
    
        
    def get_success_url(self):
        return reverse("core:judging_round_detail", kwargs={'pk':self.kwargs['jround_id']})