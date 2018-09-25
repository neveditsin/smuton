from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Criteria
from ..forms import CriteriaForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CriteriaListView(ListView):
    model = Criteria
    template_name = "core/criteria_list.html"
    paginate_by = 20
    context_object_name = "criteria_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CriteriaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CriteriaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CriteriaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CriteriaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CriteriaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CriteriaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CriteriaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CriteriaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CriteriaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CriteriaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CriteriaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CriteriaListView, self).get_template_names()


class CriteriaDetailView(DetailView):
    model = Criteria
    template_name = "core/criteria_detail.html"
    context_object_name = "criteria"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CriteriaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CriteriaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CriteriaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CriteriaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CriteriaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CriteriaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CriteriaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CriteriaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CriteriaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CriteriaDetailView, self).get_template_names()


class CriteriaCreateView(CreateView):
    model = Criteria
    form_class = CriteriaForm
    # fields = ['name', 'scale']
    template_name = "core/criteria_create.html"
    success_url = reverse_lazy("criteria_list")

    def __init__(self, **kwargs):
        return super(CriteriaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CriteriaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CriteriaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CriteriaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CriteriaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CriteriaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CriteriaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CriteriaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CriteriaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CriteriaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CriteriaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CriteriaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CriteriaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:criteria_detail", args=(self.object.pk,))


class CriteriaUpdateView(UpdateView):
    model = Criteria
    form_class = CriteriaForm
    # fields = ['name', 'scale']
    template_name = "core/criteria_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "criteria"

    def __init__(self, **kwargs):
        return super(CriteriaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CriteriaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CriteriaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CriteriaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CriteriaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CriteriaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CriteriaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CriteriaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CriteriaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CriteriaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CriteriaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CriteriaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CriteriaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CriteriaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CriteriaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CriteriaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CriteriaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:criteria_detail", args=(self.object.pk,))


class CriteriaDeleteView(DeleteView):
    model = Criteria
    template_name = "core/criteria_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "criteria"

    def __init__(self, **kwargs):
        return super(CriteriaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CriteriaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CriteriaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CriteriaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CriteriaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CriteriaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CriteriaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CriteriaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CriteriaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CriteriaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CriteriaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:criteria_list")
