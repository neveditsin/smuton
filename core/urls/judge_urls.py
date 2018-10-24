from ..views import (JudgeListView, JudgeCreateView, JudgeDetailView,
                     JudgeUpdateView, JudgeDeleteView)
from django.contrib.auth.decorators import login_required
from django.urls import re_path

urlpatterns = [
    re_path(r'^create/(?P<hack_id>\d+)/$',
        login_required(JudgeCreateView.as_view()),
        name="judge_create"),

    re_path(r'^(?P<pk>\d+)/update/$',
        login_required(JudgeUpdateView.as_view()),
        name="judge_update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(JudgeDeleteView.as_view()),
        name="judge_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        JudgeDetailView.as_view(),
        name="judge_detail"),

    re_path(r'^$',
        JudgeListView.as_view(),
        name="judge_list"),
]
