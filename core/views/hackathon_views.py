from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Hackathon
from ..forms import HackathonForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class HackathonListView(ListView):
    model = Hackathon
    template_name = "core/hackathon_list.html"
    paginate_by = 20
    context_object_name = "hackathon_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(HackathonListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(HackathonListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(HackathonListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(HackathonListView, self).get_queryset()

    def get_allow_empty(self):
        return super(HackathonListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(HackathonListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(HackathonListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(HackathonListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(HackathonListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(HackathonListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(HackathonListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(HackathonListView, self).get_template_names()


class HackathonDetailView(DetailView):
    model = Hackathon
    template_name = "core/hackathon_detail.html"
    context_object_name = "hackathon"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        return super(HackathonDetailView, self).get(request, *args, **kwargs)







class HackathonCreateView(CreateView):
    model = Hackathon
    form_class = HackathonForm
    # fields = ['name', 'desc']
    template_name = "core/hackathon_create.html"
    success_url = reverse_lazy("hackathon_list")


    def get(self, request, *args, **kwargs):
        return super(HackathonCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HackathonCreateView, self).post(request, *args, **kwargs)


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HackathonCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(HackathonCreateView, self).get_context_data(**kwargs)
        return ret

    def get_success_url(self):
        return reverse("core:hackathon_detail", args=(self.object.pk,))


class HackathonUpdateView(UpdateView):
    model = Hackathon
    form_class = HackathonForm
    # fields = ['name', 'desc']
    template_name = "core/hackathon_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "hackathon"


    def get(self, request, *args, **kwargs):
        return super(HackathonUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(HackathonUpdateView, self).post(request, *args, **kwargs)

    def get_form_kwargs(self, **kwargs):
        return super(HackathonUpdateView, self).get_form_kwargs(**kwargs)


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(HackathonUpdateView, self).form_valid(form)


    def get_success_url(self):
        return reverse("core:hackathon_detail", args=(self.object.pk,))


class HackathonDeleteView(DeleteView):
    model = Hackathon
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "hackathon"


    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(HackathonDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(HackathonDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("core:hackathon_list")
