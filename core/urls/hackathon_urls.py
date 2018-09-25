from django.conf.urls import url
from ..views import (HackathonListView, HackathonCreateView, HackathonDetailView,
                     HackathonUpdateView, HackathonDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(HackathonCreateView.as_view()),
        name="hackathon_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(HackathonUpdateView.as_view()),
        name="hackathon_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(HackathonDeleteView.as_view()),
        name="hackathon_delete"),

    url(r'^(?P<pk>\d+)/$',
        HackathonDetailView.as_view(),
        name="hackathon_detail"),

    url(r'^$',
        HackathonListView.as_view(),
        name="hackathon_list"),
]
