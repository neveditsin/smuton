from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Judge, Hackathon
from ..forms import JudgeForm, UploadFileForm
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from ..utils import csvutils
from django.views.generic import View

class JudgeListView(ListView):
    model = Judge
    template_name = "core/judge_list.html"
    context_object_name = "judge_list"
    allow_empty = True

    def get(self, request, *args, **kwargs):
        self.hid = request.GET.get('hack_id', '0')
        return super(JudgeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        if int(self.hid) > 0:
            return Judge.objects.filter(
                hackathon=self.hid
                )
        else:
            return Judge.objects.all()

    def get_allow_empty(self):
        return super(JudgeListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(JudgeListView, self).get_context_data(*args, **kwargs)
        ret['hackathon'] = Hackathon.objects.get(pk=self.hid)
        ret['file_form'] = UploadFileForm()
        return ret

    def post(self, request, *args, **kwargs):       
        self.hid = request.GET.get('hack_id', '0') 
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file']
            csvutils.import_csv_evaluators(request.FILES['file'], self.hid, True)
            
        return HttpResponseRedirect(self.get_success_url())

    
    def get_success_url(self):
        return reverse("core:judge_list") + "?hack_id=" + self.hid

class JudgeCreateView(CreateView):
    model = Judge
    form_class = JudgeForm
    template_name = "core/judge_create.html"


    def get(self, request, *args, **kwargs):
        return super(JudgeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(JudgeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(JudgeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        form = super(JudgeCreateView, self).get_form(form_class)       
        return form       

    def get_form_kwargs(self, **kwargs):
        return super(JudgeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(JudgeCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(JudgeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.hackathon = Hackathon.objects.get(pk=self.kwargs['hack_id']) 
        obj.save()
        return super(JudgeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(JudgeCreateView, self).get_context_data(**kwargs)
        ret['hackathon'] = Hackathon.objects.get(pk=self.kwargs['hack_id'])
        return ret

    def get_success_url(self):
        return reverse("core:judge_list") + "?hack_id=" + self.kwargs['hack_id']


class JudgeUpdateView(UpdateView):
    model = Judge
    form_class = JudgeForm
    template_name = "core/judge_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judge"

    def get(self, request, *args, **kwargs):
        self.hid = request.GET.get('hack_id', '0')
        return super(JudgeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.hid = request.GET.get('hack_id', '0')
        return super(JudgeUpdateView, self).post(request, *args, **kwargs)

    def form_invalid(self, form):
        return super(JudgeUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(JudgeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(JudgeUpdateView, self).get_context_data(**kwargs)
        ret['hackathon'] = Hackathon.objects.get(pk=self.hid)
        return ret

    def get_success_url(self):
        return reverse("core:judge_list") +  "?hack_id=" + self.hid


class JudgeDeleteView(DeleteView):
    model = Judge
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judge"


    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        self.hid = request.GET.get('hack_id', '0')
        return super(JudgeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(JudgeDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ret = super(JudgeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_success_url(self):
        return reverse("core:judge_list") + "?hack_id=" + self.hid
    

class JudgeDeleteAllView(View):
    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs): 
        self.hid = request.GET.get('hack_id', '0')        
        Judge.objects.filter(hackathon = Hackathon.objects.get(pk=self.hid)).delete()        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("core:judge_list")  +  "?hack_id=" + self.hid
