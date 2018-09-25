from django.conf.urls import url
from ..views import (ScaleListView, ScaleCreateView, ScaleDetailView,
                     ScaleUpdateView, ScaleDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ScaleCreateView.as_view()),
        name="scale_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ScaleUpdateView.as_view()),
        name="scale_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ScaleDeleteView.as_view()),
        name="scale_delete"),

    url(r'^(?P<pk>\d+)/$',
        ScaleDetailView.as_view(),
        name="scale_detail"),

    url(r'^$',
        ScaleListView.as_view(),
        name="scale_list"),
]
