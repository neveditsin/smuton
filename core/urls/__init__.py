from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

app_name="core"

urlpatterns = [

    url(r'^judges/', include('core.urls.judge_urls')),  # NOQA
    url(r'^teams/', include('core.urls.team_urls')),
    url(r'^scales/', include('core.urls.scale_urls')),
    url(r'^scale_entrys/', include('core.urls.scale_entry_urls')),
    url(r'^criterias/', include('core.urls.criteria_urls')),
    url(r'^hackathons/', include('core.urls.hackathon_urls')),
    url(r'^judging_rounds/', include('core.urls.judging_round_urls')),
    url(r'^judge_responses/', include('core.urls.judge_response_urls')),
    url(r'^forms/', include('core.urls.form_urls')),
    url(r'^round_results/', include('core.urls.results_urls')),
]
