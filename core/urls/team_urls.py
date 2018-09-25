from django.conf.urls import url
from ..views import (TeamListView, TeamCreateView, TeamDetailView,
                     TeamUpdateView, TeamDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(TeamCreateView.as_view()),
        name="team_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(TeamUpdateView.as_view()),
        name="team_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(TeamDeleteView.as_view()),
        name="team_delete"),

    url(r'^(?P<pk>\d+)/$',
        TeamDetailView.as_view(),
        name="team_detail"),

    url(r'^$',
        TeamListView.as_view(),
        name="team_list"),
]
