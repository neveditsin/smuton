from django.conf.urls import url
from ..views import (JudgeListView, JudgeCreateView, JudgeDetailView,
                     JudgeUpdateView, JudgeDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(JudgeCreateView.as_view()),
        name="judge_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(JudgeUpdateView.as_view()),
        name="judge_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(JudgeDeleteView.as_view()),
        name="judge_delete"),

    url(r'^(?P<pk>\d+)/$',
        JudgeDetailView.as_view(),
        name="judge_detail"),

    url(r'^$',
        JudgeListView.as_view(),
        name="judge_list"),
]
