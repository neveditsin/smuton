from django.conf.urls import url
from ..views import (JudgeResponseListView, JudgeResponseCreateView, JudgeResponseDetailView,
                     JudgeResponseDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/(?P<jround_id>\d+)$',
        login_required(JudgeResponseCreateView.as_view()),
        name="judge_response_create"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(JudgeResponseDeleteView.as_view()),
        name="judge_response_delete"),

    url(r'^(?P<pk>\d+)/$',
        JudgeResponseDetailView.as_view(),
        name="judge_response_detail"),

    url(r'^$',
        JudgeResponseListView.as_view(),
        name="judge_response_list"),
]
