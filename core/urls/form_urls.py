from django.conf.urls import url
from ..views.form_views import SumbitFormView
from ..views.form_views import DynamicFormView1
from ..views.form_views import DynamicFormView2
from django.contrib.auth.decorators import login_required

            
urlpatterns = [
    url(r'^$',
        login_required(SumbitFormView.as_view()),
        name="hackathon_form"),
		
  
]
