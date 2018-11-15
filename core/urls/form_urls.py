from django.conf.urls import url
from ..views.form_views import SumbitFormView
from django.contrib.auth.decorators import login_required

            
urlpatterns = [
    url(r'^(?P<jround_id>\d+)/$',
        login_required(SumbitFormView.as_view()),
        name="hackathon_form"),
		
  
]
