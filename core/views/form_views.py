from django.http import HttpResponse
import csv
import json
from django.views.generic import TemplateView

from ..models import Criteria, Scale, JudgingRound
from django.urls import reverse
from django.http import HttpResponseRedirect


        
class SumbitFormView(TemplateView):
    template_name = "core/form_create.html"
    
    def post(self, request, *args, **kwargs):
        p = request.POST
        i = 1 #start from name1, scale1
        while 'name'+str(i) in p:
            name = p['name'+str(i)]
            scale = p['scale'+str(i)]
            #TODO: now we update if already have it in DB. Need to throw an error    
            crit, created = Criteria.objects.update_or_create(
                name = name,
                scale = Scale.objects.get(pk=scale)
                )
            print(created)
            JudgingRound.objects.get(pk=self.kwargs['jround_id']).criteria.add(crit)
            i+=1

        return HttpResponseRedirect(self.get_success_url())
        return reverse("core:hackathon_list")
    
    def load_names(self, file_path):
        reader = csv.DictReader(open(file_path))
        for row in reader:
            name = Criteria(name=row['Name'])
            name.save()
    
    def get_criteria_names(self, request):
        #self.hid = request.GET.get('jr_id', '0')
        if request.is_ajax():
            q = request.GET.get('term', '')
            names = Criteria.objects.filter(name__icontains = q )[:20]
            results = []
            for name in names:
                name_json = {}
                name_json['name'] = name.name
                results.append(name_json)
#             drug_json['label'] = drug.short_name
#             drug_json['value'] = drug.short_name
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
    
    def get_context_data(self, *args, **kwargs):        
        ret = super(SumbitFormView, self).get_context_data(*args, **kwargs)
        ret['scale'] = Scale.objects.all()
        return ret
    
        
    def get_success_url(self):
        return reverse("core:judging_round_detail", kwargs={'pk':self.kwargs['jround_id']})