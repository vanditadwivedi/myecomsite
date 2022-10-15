
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shop home"),
    path("about/", views.about, name="about us"),
    path("tracker/", views.tracker, name="tracker"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("checkout/", views.checkout, name="checkout"),
    path("prodview/<int:myid>", views.prodview, name="prodview"),
]
