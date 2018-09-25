from django.conf.urls import url
from ..views import (JudgingRoundListView, JudgingRoundCreateView, JudgingRoundDetailView,
                     JudgingRoundUpdateView, JudgingRoundDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(JudgingRoundCreateView.as_view()),
        name="judging_round_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(JudgingRoundUpdateView.as_view()),
        name="judging_round_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(JudgingRoundDeleteView.as_view()),
        name="judging_round_delete"),

    url(r'^(?P<pk>\d+)/$',
        JudgingRoundDetailView.as_view(),
        name="judging_round_detail"),

    url(r'^$',
        JudgingRoundListView.as_view(),
        name="judging_round_list"),
]
