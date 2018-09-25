from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import JudgingRound
from ..forms import JudgingRoundForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class JudgingRoundListView(ListView):
    model = JudgingRound
    template_name = "core/judging_round_list.html"
    paginate_by = 20
    context_object_name = "judging_round_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(JudgingRoundListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgingRoundListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgingRoundListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(JudgingRoundListView, self).get_queryset()

    def get_allow_empty(self):
        return super(JudgingRoundListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(JudgingRoundListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(JudgingRoundListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(JudgingRoundListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(JudgingRoundListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(JudgingRoundListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgingRoundListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgingRoundListView, self).get_template_names()


class JudgingRoundDetailView(DetailView):
    model = JudgingRound
    template_name = "core/judging_round_detail.html"
    context_object_name = "judging_round"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(JudgingRoundDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgingRoundDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgingRoundDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgingRoundDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgingRoundDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgingRoundDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(JudgingRoundDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgingRoundDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgingRoundDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgingRoundDetailView, self).get_template_names()


class JudgingRoundCreateView(CreateView):
    model = JudgingRound
    form_class = JudgingRoundForm
    # fields = ['hackathon', 'number']
    template_name = "core/judging_round_create.html"
    success_url = reverse_lazy("judging_round_list")

    def __init__(self, **kwargs):
        return super(JudgingRoundCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(JudgingRoundCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgingRoundCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(JudgingRoundCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(JudgingRoundCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(JudgingRoundCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(JudgingRoundCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(JudgingRoundCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(JudgingRoundCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(JudgingRoundCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(JudgingRoundCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(JudgingRoundCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgingRoundCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judging_round_detail", args=(self.object.pk,))


class JudgingRoundUpdateView(UpdateView):
    model = JudgingRound
    form_class = JudgingRoundForm
    # fields = ['hackathon', 'number']
    template_name = "core/judging_round_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judging_round"

    def __init__(self, **kwargs):
        return super(JudgingRoundUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgingRoundUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(JudgingRoundUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(JudgingRoundUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgingRoundUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgingRoundUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgingRoundUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(JudgingRoundUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(JudgingRoundUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(JudgingRoundUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(JudgingRoundUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(JudgingRoundUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(JudgingRoundUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(JudgingRoundUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgingRoundUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgingRoundUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgingRoundUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judging_round_detail", args=(self.object.pk,))


class JudgingRoundDeleteView(DeleteView):
    model = JudgingRound
    template_name = "core/judging_round_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judging_round"

    def __init__(self, **kwargs):
        return super(JudgingRoundDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(JudgingRoundDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(JudgingRoundDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(JudgingRoundDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(JudgingRoundDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(JudgingRoundDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(JudgingRoundDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(JudgingRoundDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(JudgingRoundDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(JudgingRoundDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(JudgingRoundDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:judging_round_list")
