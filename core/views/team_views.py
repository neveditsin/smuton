from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Team
from ..forms import TeamForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class TeamListView(ListView):
    model = Team
    template_name = "core/team_list.html"
    paginate_by = 20
    context_object_name = "team_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(TeamListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TeamListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TeamListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(TeamListView, self).get_queryset()

    def get_allow_empty(self):
        return super(TeamListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(TeamListView, self).get_context_data(*args, **kwargs)
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


class TeamDetailView(DetailView):
    model = Team
    template_name = "core/team_detail.html"
    context_object_name = "team"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(TeamDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TeamDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TeamDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TeamDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(TeamDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(TeamDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(TeamDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TeamDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TeamDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TeamDetailView, self).get_template_names()


class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    # fields = ['name', 'participants']
    template_name = "core/team_create.html"
    success_url = reverse_lazy("team_list")

    def __init__(self, **kwargs):
        return super(TeamCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(TeamCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TeamCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TeamCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(TeamCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(TeamCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(TeamCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(TeamCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(TeamCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TeamCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TeamCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(TeamCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TeamCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:team_detail", args=(self.object.pk,))


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

    def __init__(self, **kwargs):
        return super(TeamUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TeamUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(TeamUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(TeamUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TeamUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(TeamUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(TeamUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(TeamUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(TeamUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(TeamUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(TeamUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(TeamUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(TeamUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(TeamUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TeamUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TeamUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TeamUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:team_detail", args=(self.object.pk,))


class TeamDeleteView(DeleteView):
    model = Team
    template_name = "core/team_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "team"

    def __init__(self, **kwargs):
        return super(TeamDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(TeamDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(TeamDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(TeamDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(TeamDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(TeamDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(TeamDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(TeamDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(TeamDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(TeamDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(TeamDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:team_list")
