from django.urls import re_path
from ..views import (JudgingRoundListView, JudgingRoundCreateView, JudgingRoundDetailView,
                     JudgingRoundDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    re_path(r'^create/(?P<hack_id>\d+)/$',  # NOQA
        login_required(JudgingRoundCreateView.as_view()),
        name="judging_round_create"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(JudgingRoundDeleteView.as_view()),
        name="judging_round_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        JudgingRoundDetailView.as_view(),
        name="judging_round_detail"),

    re_path(r'^$',
        JudgingRoundListView.as_view(),
        name="judging_round_list"),
    
]
