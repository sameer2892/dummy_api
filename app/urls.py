from django.conf.urls import url
from app import views

app_name = "app"
urlpatterns = [
    url(r'^get_data$', views.get_all_venues_events, name="get_all_venues_events"),
    url(r'^get_venue$', views.get_venue, name="get_venue"),
    url(r'^get_event$', views.get_event, name="get_event"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login")
]