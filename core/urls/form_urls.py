from django.conf.urls import url
from ..views.form_views import SumbitFormView, PaperFormView
from django.contrib.auth.decorators import login_required

            
urlpatterns = [
    url(r'^(?P<jround_id>\d+)/$',
        login_required(SumbitFormView.as_view()),
        name="hackathon_form"),
		
      url(r'^(?P<jround_id>\d+)/paper_forms$',
        login_required(PaperFormView.as_view()),
        name="paper_form"),
]
