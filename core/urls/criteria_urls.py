from django.conf.urls import url
from ..views import (CriteriaListView, CriteriaCreateView, CriteriaDetailView,
                     CriteriaUpdateView, CriteriaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CriteriaCreateView.as_view()),
        name="criteria_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CriteriaUpdateView.as_view()),
        name="criteria_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CriteriaDeleteView.as_view()),
        name="criteria_delete"),

    url(r'^(?P<pk>\d+)/$',
        CriteriaDetailView.as_view(),
        name="criteria_detail"),

    url(r'^$',
        CriteriaListView.as_view(),
        name="criteria_list"),
]
