from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from ..models import JudgeResponse, JudgingRound
from ..forms import JudgeResponseForm, JudgeResponseFormHead
from django.urls import reverse
from django.http import HttpResponseRedirect


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


    def get_context_data(self, **kwargs):
        ret = super(JudgeResponseDetailView, self).get_context_data(**kwargs)
        return ret


    def get_template_names(self):
        return super(JudgeResponseDetailView, self).get_template_names()


class JudgeResponseCreateView(TemplateView):
    template_name = "core/judge_response_create.html"
       
    def __init__(self, **kwargs):
        return super(JudgeResponseCreateView, self).__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.jr = JudgingRound.objects.get(pk=kwargs['jround_id']) 
        self.head_form = JudgeResponseFormHead(self.jr)       
        self.forms = []
        for cr in self.jr.criteria.all():
            self.forms.append(JudgeResponseForm(cr, prefix=cr.pk))
        return super(JudgeResponseCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return HttpResponseRedirect(self.get_success_url())


    def get_context_data(self, **kwargs):
        ret = super(JudgeResponseCreateView, self).get_context_data(**kwargs)
        ret['jround'] = self.jr
        ret['head_form'] = self.head_form
        ret['forms'] = self.forms
        return ret
 
    def get_success_url(self):
        return reverse("core:judging_round_detail", kwargs={'pk':self.kwargs['jround_id']})



class JudgeResponseDeleteView(DeleteView):
    model = JudgeResponse
    template_name = "core/judge_response_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "judge_response"

    def get_success_url(self):
        return reverse("core:judge_response_list")
