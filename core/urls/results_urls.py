from django.conf.urls import url
from ..views.results_views import RoundResultsView
from django.contrib.auth.decorators import login_required

            
urlpatterns = [
    url(r'^(?P<jround_id>\d+)/$',
        login_required(RoundResultsView.as_view()),
        name="round_results"),
		
  
]
