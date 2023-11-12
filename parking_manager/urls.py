from django.urls import path

from parking_manager import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("payment", views.payment, name="payment"),
    path("res_cancel_confirmation", views.res_cancel_confirmation, name="res_cancel_confirmation"),
    path("res_cancellation", views.res_cancellation, name="res_cancellation"),
    path("res_confirmation", views.res_confirmation, name="res_confirmation"),
    path("res_mod_confirmation", views.res_mod_confirmation, name="res_mod_confirmation"),
    path("res_modification", views.res_modification, name="res_modification"),
    path("reservation", views.reservation, name="reservation"),
    path("res_modification_detail", views.res_modification_detail, name="res_modification_detail"),


]