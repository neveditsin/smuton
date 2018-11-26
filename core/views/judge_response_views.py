from django.views.generic import TemplateView, DeleteView
from ..models import JudgeResponse, JudgingRound, Responses
from ..forms import JudgeResponseForm, JudgeResponseFormHead
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages
import pandas as pd


class JudgeResponseListView(TemplateView):
    template_name = "core/judge_response_list.html"

    def get(self, request, *args, **kwargs):
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        return super(JudgeResponseListView, self).get(request, *args, **kwargs)



    def get_context_data(self, *args, **kwargs):
        ret = super(JudgeResponseListView, self).get_context_data(*args, **kwargs)
        df = pd.DataFrame.from_records(Responses.objects.\
            filter(round_id=self.jr.pk).\
            values('judge_name', 'team_name', 'criteria', 'mark'))
        
        pt = pd.DataFrame(df.pivot_table(index=['judge_name', 'team_name'], 
                                         columns='criteria', 
                                         values='mark', 
                                         aggfunc='first').to_records())


        ret['resps'] = pt.to_html()        
        ret['jround'] = self.jr
        return ret



class JudgeResponseLanding(TemplateView):
    template_name = "core/judge_response_landing.html"

    def __init__(self, **kwargs):
        return super(JudgeResponseLanding, self).__init__(**kwargs)


    def get_context_data(self, **kwargs):
        ret = super(JudgeResponseLanding, self).get_context_data(**kwargs)
        return ret


class JudgeResponseCreateView(TemplateView):
    template_name = "core/judge_response_create.html"
       

    def get(self, request, *args, **kwargs):
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        self.head_form = JudgeResponseFormHead(self.jr)       
        self.forms = []
        for cr in self.jr.criteria.all():
            self.forms.append(JudgeResponseForm(cr, prefix=cr.pk))
        return super(JudgeResponseCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        judge_team = JudgeResponseFormHead(jr,request.POST)
        if judge_team.is_valid():
            post_judge = judge_team.cleaned_data['judge']
            post_team = judge_team.cleaned_data['team']
        else:
            return HttpResponse(status=500)
        #existing_resps = JudgeResponse.objects.filter(round = jr, judge=post_judge)
        #print(existing_resps)
        try:
            for cr in jr.criteria.all():
                mark = JudgeResponseForm(cr, request.POST, prefix=cr.pk)
                if mark.is_valid():      
                    JudgeResponse.objects.create(
                        round = jr,
                        team = post_team,
                        judge = post_judge,
                        criterion = cr,
                        mark = mark.cleaned_data['mark'],
                        )
                else:
                    return HttpResponse(status=500)
        except IntegrityError:
            messages.error(request, "You have already submitted a response for team " + str(post_team))
            return HttpResponseRedirect(request.path)
                    
        return HttpResponseRedirect(self.get_success_url())


    def get_context_data(self, **kwargs):
        ret = super(JudgeResponseCreateView, self).get_context_data(**kwargs)
        ret['jround'] = self.jr
        ret['head_form'] = self.head_form
        ret['forms'] = self.forms
        return ret
 
    def get_success_url(self):
        return reverse("core:judge_response_landing", kwargs={'jround_id':self.kwargs['jround_id']})
    
    
    
class JudgeResponseDeleteView(DeleteView):
    model = JudgeResponse
    template_name = "core/judge_response_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judge_response"

    def get_success_url(self):
        return reverse("core:judge_response_list", kwargs={'jround_id':self.kwargs['jround_id']})
