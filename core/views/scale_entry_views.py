from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import ScaleEntry, Scale
from ..forms import ScaleEntryForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class ScaleEntryListView(ListView):
    model = ScaleEntry
    template_name = "core/scale_entry_list.html"
    context_object_name = "scale_entry_list"
    allow_empty = True

    def get(self, request, *args, **kwargs):
        self.scale = Scale.objects.get(pk=kwargs['scale_id'])
        return super(ScaleEntryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return ScaleEntry.objects.filter(
                scale=self.scale
                )


    def get_context_data(self, *args, **kwargs):
        ret = super(ScaleEntryListView, self).get_context_data(*args, **kwargs)
        ret['scale'] = self.scale
        return ret




class ScaleEntryCreateView(CreateView):
    model = ScaleEntry
    form_class = ScaleEntryForm
    # fields = ['entry', 'weight', 'scale']
    template_name = "core/scale_entry_create.html"

    def get(self, request, *args, **kwargs):
        self.scale = Scale.objects.get(pk=kwargs['scale_id'])
        return super(ScaleEntryCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.scale = Scale.objects.get(pk=kwargs['scale_id'])
        return super(ScaleEntryCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ScaleEntryCreateView, self).get_form_class()

    def get_initial(self):
        return super(ScaleEntryCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ScaleEntryCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.scale = self.scale
        obj.save()
        return super(ScaleEntryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ScaleEntryCreateView, self).get_context_data(**kwargs)
        ret['scale'] = self.scale
        return ret

    def get_success_url(self):
        return reverse("core:scale_entry_list", args=(self.scale.pk,))


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

    def get(self, request, *args, **kwargs):
        return super(ScaleEntryUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ScaleEntryUpdateView, self).post(request, *args, **kwargs)

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

    def get_success_url(self):
        return reverse("core:scale_entry_list", args=(self.object.scale.pk,))


class ScaleEntryDeleteView(DeleteView):
    model = ScaleEntry
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "scale_entry"

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        self.scale = ScaleEntry.objects.get(pk=kwargs['pk']).scale
        return super(ScaleEntryDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ScaleEntryDeleteView, self).delete(request, *args, **kwargs)


    def get_success_url(self):
        return reverse("core:scale_entry_list", kwargs={'scale_id':self.scale.pk})
