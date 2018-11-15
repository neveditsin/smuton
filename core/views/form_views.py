#from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
import json
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.template.context_processors import request
from core import models
#from django.views.generic.edit import CreateView

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Criteria, Scale
from ..forms import CriteriaForm, DynamicForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


        
class SumbitFormView(TemplateView):
    template_name = "core/form_create.html"
    
    def dynamicformpage1(self, request, *args, **kwargs):
        return render(request, 'DynamicFormPage1.html')
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
#         c=Criteria(name=request.POST.get('name'))
#         c.save()
#         s=Criteria(scale=request.POST.get('scale'))
#         s.save()
        form = CriteriaForm(request.POST)
        if form.is_valid():
            form.create(name=form.cleaned_data["name"],scale=form.cleaned_data["scale"])
#            form.save()
#             name=form.cleaned_data['name']
#             scale=form.cleaned_data['scale']
#             p=Criteria(name=name, scale=scale)
#             p.save()


        #criteria_name = request.POST.get('name'+i)
        return render(request, self.template_name, {'form': form})
    
    def load_names(self, file_path):
        reader = csv.DictReader(open(file_path))
        for row in reader:
            name = Criteria(name=row['Name'])
            name.save()
    
    def get_criteria_names(self, request):
        self.hid = request.GET.get('jr_id', '0')
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
    
    
class DynamicFormView1(View):#CreateView? Check all available views  try
    template_name = "core/DynamicFormPage1.html"
    
    
    def get(self, request, *args, **kwargs):
        form = DynamicForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = DynamicForm(request.POST)
        
        if form.is_valid():
            data = request.POST.copy()
            form = DynamicForm()
            
        if request.method == 'POST':
            form = DynamicForm(request.POST)
            
        
        args = {'form': form, 'data':data}
        models.Criteria.objects.all()
        models.Scale.objects.all()
        print(request.POST)
        return render(request, self.template_name, args)
        #return render(request, self.template_name, answer)
        #return super(DynamicFormView, self).post(request, *args, **kwargs)
        
class DynamicFormView2(CreateView):#CreateView? Check all available views  try
    template_name = "core/DynamicFormPage2.html"
    model = Criteria
    form_class = DynamicForm
    success_url = reverse_lazy("dynamic2")


