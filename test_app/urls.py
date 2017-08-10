from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /polls/
    url(r'^$',      	views.index2,    name='index'),
    url(r'^login/',      views.index3,    name='index3'), 
 ]
