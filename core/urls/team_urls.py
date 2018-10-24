from django.urls import re_path
from ..views import (TeamListView, TeamCreateView, TeamDetailView,
                     TeamUpdateView, TeamDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    re_path(r'^create/(?P<hack_id>\d+)/$',
        login_required(TeamCreateView.as_view()),
        name="team_create"),

    re_path(r'^(?P<pk>\d+)/update/$',
        login_required(TeamUpdateView.as_view()),
        name="team_update"),

    re_path(r'^(?P<pk>\d+)/delete/$',
        login_required(TeamDeleteView.as_view()),
        name="team_delete"),

    re_path(r'^(?P<pk>\d+)/$',
        TeamDetailView.as_view(),
        name="team_detail"),

    re_path(r'^$',
        TeamListView.as_view(),
        name="team_list"),
]
