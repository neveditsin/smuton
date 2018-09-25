from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Judge
from ..forms import JudgeForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class JudgeListView(ListView):
    model = Judge
    template_name = "core/judge_list.html"
    paginate_by = 20
    context_object_name = "judge_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(JudgeListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgeListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(JudgeListView, self).get_queryset()

    def get_allow_empty(self):
        return super(JudgeListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(JudgeListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(JudgeListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(JudgeListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(JudgeListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(JudgeListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeListView, self).get_template_names()


class JudgeDetailView(DetailView):
    model = Judge
    template_name = "core/judge_detail.html"
    context_object_name = "judge"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(JudgeDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgeDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgeDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgeDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgeDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgeDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(JudgeDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgeDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeDetailView, self).get_template_names()


class JudgeCreateView(CreateView):
    model = Judge
    form_class = JudgeForm
    # fields = ['first_name', 'last_name', 'email']
    template_name = "core/judge_create.html"
    success_url = reverse_lazy("judge_list")

    def __init__(self, **kwargs):
        return super(JudgeCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(JudgeCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(JudgeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(JudgeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(JudgeCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(JudgeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(JudgeCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(JudgeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(JudgeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(JudgeCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judge_detail", args=(self.object.pk,))


class JudgeUpdateView(UpdateView):
    model = Judge
    form_class = JudgeForm
    # fields = ['first_name', 'last_name', 'email']
    template_name = "core/judge_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judge"

    def __init__(self, **kwargs):
        return super(JudgeUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgeUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(JudgeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgeUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgeUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgeUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(JudgeUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(JudgeUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(JudgeUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(JudgeUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(JudgeUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(JudgeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(JudgeUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgeUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judge_detail", args=(self.object.pk,))


class JudgeDeleteView(DeleteView):
    model = Judge
    template_name = "core/judge_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judge"

    def __init__(self, **kwargs):
        return super(JudgeDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgeDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(JudgeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(JudgeDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgeDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgeDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgeDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(JudgeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgeDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judge_list")
