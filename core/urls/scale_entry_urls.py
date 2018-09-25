from django.conf.urls import url
from ..views import (ScaleEntryListView, ScaleEntryCreateView, ScaleEntryDetailView,
                     ScaleEntryUpdateView, ScaleEntryDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ScaleEntryCreateView.as_view()),
        name="scale_entry_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ScaleEntryUpdateView.as_view()),
        name="scale_entry_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ScaleEntryDeleteView.as_view()),
        name="scale_entry_delete"),

    url(r'^(?P<pk>\d+)/$',
        ScaleEntryDetailView.as_view(),
        name="scale_entry_detail"),

    url(r'^$',
        ScaleEntryListView.as_view(),
        name="scale_entry_list"),
]
