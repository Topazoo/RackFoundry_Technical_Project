from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^marvel/$', views.marvel_home, name='marvel_home'),
    url(r'^tickets/$', views.tickets_home, name='tickets_home'),
    url(r'^tickets/receive/$', views.receive_ticket, name="receive_ticket"),
    url(r'^tickets/(?P<ticket>\d{3}-\d{3})/$', views.get_ticket_id, name="get_ticket"),
    url(r'^tickets/team/(?P<team>\w+)/$', views.get_tickets_team, name="get_tickets_team"),
    url(r'^tickets/priority/(?P<priority>\w+)/$', views.get_tickets_priority, name="get_tickets_priority")
]
