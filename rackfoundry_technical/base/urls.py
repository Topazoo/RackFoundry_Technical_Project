from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^marvel/$', views.marvel_home, name='marvel_home'),
    url(r'^tickets/$', views.tickets_home, name='tickets_home'),
    url(r'^tickets/receive/*', views.receive_ticket, name="receive_ticket")
]
