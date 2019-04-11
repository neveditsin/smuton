from django.views.generic import TemplateView

from ..models import JudgingRound, Team
from ..utils import csvutils
from django.urls import reverse
from core.models import Responses
from core.utils.aggregator import Agg
from django.http import HttpResponseRedirect
from ..forms import UploadFileForm

class RoundResultsView(TemplateView):
    template_name = "core/round_results.html"
    
    def get(self, request, *args, **kwargs):        
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        return super(RoundResultsView, self).get(request, *args, **kwargs)    

    def post(self, request, *args, **kwargs):        
        form = UploadFileForm(request.POST, request.FILES)
        
        
        if form.is_valid():
            request.FILES['file']
            csvutils.import_csv_simple(request.FILES['file'], kwargs['jround_id'], True)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *args, **kwargs):        
        ret = super(RoundResultsView, self).get_context_data(*args, **kwargs)
        result = Agg.aggregate(Responses, self.jr.hackathon.pk, self.jr.number, 'mean')        
        ret['jround'] = self.jr 
        result['team_id'] = result['team_id'].apply(lambda tid: Team.objects.get(pk=tid).name)
        result.insert(0, 'rank', range(1, 1 + len(result)))
        result = result.rename(index=str, columns={"team_id": "team", "judge_id_count": "judges number"})
        ret['result'] = result.to_html(index=False)
        return ret
    
        
    def get_success_url(self):
        return reverse("core:judging_round_detail", kwargs={'pk':self.kwargs['jround_id']})