from django.http import HttpResponse
from django.views.generic import TemplateView

from ..models import Criteria, Scale, JudgingRound
from django.urls import reverse
from django.http import HttpResponseRedirect


        
class RoundResultsView(TemplateView):
    template_name = "core/round_results.html"
    
    def get(self, request, *args, **kwargs):        
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        return super(RoundResultsView, self).get(request, *args, **kwargs)    

    def get_context_data(self, *args, **kwargs):        
        ret = super(RoundResultsView, self).get_context_data(*args, **kwargs)
        ret['jround'] = self.jr
        return ret
    
        
    def get_success_url(self):
        return reverse("core:judging_round_detail", kwargs={'pk':self.kwargs['jround_id']})