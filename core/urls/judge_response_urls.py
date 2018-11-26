from django.conf.urls import url
from ..views import (JudgeResponseListView, JudgeResponseCreateView, JudgeResponseLanding
                     )
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/(?P<jround_id>\d+)$',
        login_required(JudgeResponseCreateView.as_view()),
        name="judge_response_create"),

    url(r'^(?P<jround_id>\d+)/$',
        JudgeResponseLanding.as_view(),
        name="judge_response_landing"),

    url(r'^list/(?P<jround_id>\d+)$',
        JudgeResponseListView.as_view(),
        name="judge_response_list"),
    


]
