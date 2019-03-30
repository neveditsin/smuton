from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import View
from ..models import Team, Hackathon
from ..forms import TeamForm, UploadFileForm
from django.urls import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from ..utils import csvutils

class TeamListView(ListView):
    model = Team
    template_name = "core/team_list.html"
    context_object_name = "team_list"
    allow_empty = True
    hid = 0
    

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
        #return reverse("core:team_list")  +  "?hack_id=" + self.hid
        return super(TeamDeleteView, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ret = super(TeamDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_success_url(self):
        return reverse("core:team_list")  +  "?hack_id=" + self.hid


class TeamDeleteAllView(View):
    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs): 
        self.hid = request.GET.get('hack_id', '0')        
        Team.objects.filter(hackathon = Hackathon.objects.get(pk=self.hid)).delete()        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("core:team_list")  +  "?hack_id=" + self.hid

