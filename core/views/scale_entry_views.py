from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import ScaleEntry
from ..forms import ScaleEntryForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class ScaleEntryListView(ListView):
    model = ScaleEntry
    template_name = "core/scale_entry_list.html"
    paginate_by = 20
    context_object_name = "scale_entry_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ScaleEntryListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ScaleEntryListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ScaleEntryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ScaleEntryListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ScaleEntryListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ScaleEntryListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ScaleEntryListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ScaleEntryListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ScaleEntryListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ScaleEntryListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ScaleEntryListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScaleEntryListView, self).get_template_names()


class ScaleEntryDetailView(DetailView):
    model = ScaleEntry
    template_name = "core/scale_entry_detail.html"
    context_object_name = "scale_entry"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ScaleEntryDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ScaleEntryDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ScaleEntryDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ScaleEntryDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ScaleEntryDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ScaleEntryDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ScaleEntryDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ScaleEntryDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ScaleEntryDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScaleEntryDetailView, self).get_template_names()


class ScaleEntryCreateView(CreateView):
    model = ScaleEntry
    form_class = ScaleEntryForm
    # fields = ['entry', 'weight', 'scale']
    template_name = "core/scale_entry_create.html"
    success_url = reverse_lazy("scale_entry_list")

    def __init__(self, **kwargs):
        return super(ScaleEntryCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ScaleEntryCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ScaleEntryCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ScaleEntryCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ScaleEntryCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ScaleEntryCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ScaleEntryCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ScaleEntryCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ScaleEntryCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ScaleEntryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ScaleEntryCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ScaleEntryCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScaleEntryCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:scale_entry_detail", args=(self.object.pk,))


class ScaleEntryUpdateView(UpdateView):
    model = ScaleEntry
    form_class = ScaleEntryForm
    # fields = ['entry', 'weight', 'scale']
    template_name = "core/scale_entry_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "scale_entry"

    def __init__(self, **kwargs):
        return super(ScaleEntryUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ScaleEntryUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ScaleEntryUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ScaleEntryUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ScaleEntryUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ScaleEntryUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ScaleEntryUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ScaleEntryUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ScaleEntryUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ScaleEntryUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ScaleEntryUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ScaleEntryUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ScaleEntryUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ScaleEntryUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ScaleEntryUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ScaleEntryUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScaleEntryUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:scale_entry_detail", args=(self.object.pk,))


class ScaleEntryDeleteView(DeleteView):
    model = ScaleEntry
    template_name = "core/scale_entry_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "scale_entry"

    def __init__(self, **kwargs):
        return super(ScaleEntryDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ScaleEntryDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ScaleEntryDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ScaleEntryDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ScaleEntryDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ScaleEntryDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ScaleEntryDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ScaleEntryDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ScaleEntryDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ScaleEntryDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ScaleEntryDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:scale_entry_list")
