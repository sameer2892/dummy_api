from django.conf.urls import url
from app import views

app_name = "app"
urlpatterns = [
    url(r'^get_data$', views.get_data, name="get_all_venues_events")
    # url(r'^get_venue$', views.get_venue, name="get_venue"),
    # url(r'^get_event$', views.get_event, name="get_event"),
    # url(r'^register$', views.register, name="register"),
    # url(r'^login$', views.login, name="login"),
    # url(r'^get_menu$', views.get_menu, name="get_menu"),
    # url(r'^get_card$', views.get_card, name="get_card"),
    # url(r'^get_table$', views.get_table, name="get_table"),
    # url(r'^get_package$', views.get_package, name="get_package"),
    # url(r'^get_ticket$', views.get_ticket, name="get_ticket"),
    # url(r'^get_all_cities$', views.get_all_cities, name="get_all_cities")
]