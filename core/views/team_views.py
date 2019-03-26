from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Team, Hackathon
from ..forms import TeamForm, UploadFileForm
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from ..utils import csvutils

class TeamListView(ListView):
    model = Team
    template_name = "core/team_list.html"
    paginate_by = 20
    context_object_name = "team_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0
    hid = 0
    
    def __init__(self, **kwargs):
        return super(TeamListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TeamListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.hid = request.GET.get('hack_id', '0')
        return super(TeamListView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):       
        self.hid = request.GET.get('hack_id', '0') 
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            request.FILES['file']
            csvutils.import_csv_teams(request.FILES['file'], self.hid, True)
            
        return HttpResponseRedirect(self.get_success_url())

    def get_queryset(self):
        if int(self.hid) > 0:
            return Team.objects.filter(
                hackathon=self.hid
                )
        else:
            return Team.objects.all()

    def get_allow_empty(self):
        return super(TeamListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(TeamListView, self).get_context_data(*args, **kwargs)
        ret['hackathon'] = Hackathon.objects.get(pk=self.hid)
        ret['file_form'] = UploadFileForm()
        return ret

    def get_paginate_by(self, queryset):
        return super(TeamListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(TeamListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(TeamListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(TeamListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(TeamListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TeamListView, self).get_template_names()


    def get_success_url(self):
        return reverse("core:team_list") + "?hack_id=" + self.hid

class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    # fields = ['name', 'participants']
    template_name = "core/team_create.html"

    def get(self, request, *args, **kwargs):
        return super(TeamCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TeamCreateView, self).post(request, *args, **kwargs)

    def get_initial(self):
        return super(TeamCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(TeamCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.hackathon = Hackathon.objects.get(pk=self.kwargs['hack_id']) 
        obj.save()
        return super(TeamCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TeamCreateView, self).get_context_data(**kwargs)
        ret['hackathon'] = Hackathon.objects.get(pk=self.kwargs['hack_id'])        
        return ret

    def get_success_url(self):
        return reverse("core:team_list") + "?hack_id=" + self.kwargs['hack_id']


class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    # fields = ['name', 'participants']
    template_name = "core/team_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "team"


    def get(self, request, *args, **kwargs):
        self.hid = request.GET.get('hack_id', '0')        
        return super(TeamUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.hid = request.GET.get('hack_id', '0')        
        return super(TeamUpdateView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TeamUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TeamUpdateView, self).get_context_data(**kwargs)
        ret['hackathon'] = Hackathon.objects.get(pk=self.hid) 
        return ret

    def get_success_url(self):
        return reverse("core:team_list")  +  "?hack_id=" + self.hid


class TeamDeleteView(DeleteView):
    model = Team
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "team"

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        self.hid = request.GET.get('hack_id', '0')        
        return super(TeamDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(TeamDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ret = super(TeamDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_success_url(self):
        return reverse("core:team_list")  +  "?hack_id=" + self.hid
