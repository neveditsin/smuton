from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import JudgeResponse
from ..forms import JudgeResponseForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class JudgeResponseListView(ListView):
    model = JudgeResponse
    template_name = "core/judge_response_list.html"
    paginate_by = 20
    context_object_name = "judge_response_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(JudgeResponseListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgeResponseListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgeResponseListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(JudgeResponseListView, self).get_queryset()

    def get_allow_empty(self):
        return super(JudgeResponseListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(JudgeResponseListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(JudgeResponseListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(JudgeResponseListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(JudgeResponseListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(JudgeResponseListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeResponseListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeResponseListView, self).get_template_names()


class JudgeResponseDetailView(DetailView):
    model = JudgeResponse
    template_name = "core/judge_response_detail.html"
    context_object_name = "judge_response"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(JudgeResponseDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgeResponseDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgeResponseDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgeResponseDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgeResponseDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgeResponseDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(JudgeResponseDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgeResponseDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeResponseDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeResponseDetailView, self).get_template_names()


class JudgeResponseCreateView(CreateView):
    model = JudgeResponse
    form_class = JudgeResponseForm
    # fields = ['round', 'judge', 'team', 'criterion', 'mark']
    template_name = "core/judge_response_create.html"
    success_url = reverse_lazy("judge_response_list")

    def __init__(self, **kwargs):
        return super(JudgeResponseCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(JudgeResponseCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgeResponseCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(JudgeResponseCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(JudgeResponseCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(JudgeResponseCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(JudgeResponseCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(JudgeResponseCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(JudgeResponseCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(JudgeResponseCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(JudgeResponseCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeResponseCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeResponseCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judge_response_detail", args=(self.object.pk,))


class JudgeResponseUpdateView(UpdateView):
    model = JudgeResponse
    form_class = JudgeResponseForm
    # fields = ['round', 'judge', 'team', 'criterion', 'mark']
    template_name = "core/judge_response_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judge_response"

    def __init__(self, **kwargs):
        return super(JudgeResponseUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgeResponseUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgeResponseUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(JudgeResponseUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgeResponseUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgeResponseUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgeResponseUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(JudgeResponseUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(JudgeResponseUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(JudgeResponseUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(JudgeResponseUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(JudgeResponseUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(JudgeResponseUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(JudgeResponseUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgeResponseUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeResponseUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeResponseUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judge_response_detail", args=(self.object.pk,))


class JudgeResponseDeleteView(DeleteView):
    model = JudgeResponse
    template_name = "core/judge_response_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judge_response"

    def __init__(self, **kwargs):
        return super(JudgeResponseDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgeResponseDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(JudgeResponseDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(JudgeResponseDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgeResponseDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgeResponseDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgeResponseDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(JudgeResponseDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgeResponseDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgeResponseDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgeResponseDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judge_response_list")
