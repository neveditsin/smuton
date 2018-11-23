from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Scale
from ..forms import ScaleForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class ScaleListView(ListView):
    model = Scale
    template_name = "core/scale_list.html"
    paginate_by = 20
    context_object_name = "scale_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        return super(ScaleListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ScaleListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ScaleListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ScaleListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ScaleListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ScaleListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ScaleListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ScaleListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)



class ScaleDetailView(DetailView):
    model = Scale
    template_name = "core/scale_detail.html"
    context_object_name = "scale"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

   
    def get(self, request, *args, **kwargs):
        return super(ScaleDetailView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ScaleDetailView, self).get_queryset()

    def get_context_data(self, **kwargs):
        ret = super(ScaleDetailView, self).get_context_data(**kwargs)
        return ret


class ScaleCreateView(CreateView):
    model = Scale
    form_class = ScaleForm
    # fields = ['name']
    template_name = "core/scale_create.html"
    success_url = reverse_lazy("scale_list")

  
    def get(self, request, *args, **kwargs):
        return super(ScaleCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ScaleCreateView, self).post(request, *args, **kwargs)

    def form_invalid(self, form):
        return super(ScaleCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ScaleCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ScaleCreateView, self).get_context_data(**kwargs)
        return ret

    def get_success_url(self):
        return reverse("core:scale_list")


class ScaleUpdateView(UpdateView):
    model = Scale
    form_class = ScaleForm
    # fields = ['name']
    template_name = "core/scale_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "scale"

    def get(self, request, *args, **kwargs):
        return super(ScaleUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ScaleUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ScaleUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ScaleUpdateView, self).get_queryset()

    def get_form(self, form_class=None):
        return super(ScaleUpdateView, self).get_form(form_class)


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ScaleUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ScaleUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_success_url(self):
        return reverse("core:scale_list")


class ScaleDeleteView(DeleteView):
    model = Scale
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "scale"


    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ScaleDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ScaleDeleteView, self).delete(request, *args, **kwargs)


    def get_success_url(self):
        return reverse("core:scale_list")
