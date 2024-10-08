from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user", views.user, name="user"),
    path("about-me", views.about_me, name="about_me"),
    path("about-site", views.about_site, name="about_site"),
    path("tools", views.tools, name="tools"),
    path("tools/popup-maker", views.popup_maker, name="popup_maker"),
    path("shrek-fanpage", views.shrek_fanpage, name="shrek_fanpage"),
    path("games", views.error503, name="games"),
    path("games/clicker", views.error503, name="clicker"),
    path("school-stuff/computing-innovation", views.computing_innovation, name="computing_innovation"),
    path("school-stuff/congo-act-now", views.congo_act_now, name="congo_act_now"),
    path("school-stuff/nc-colonial-marketing", views.nc_colonial_marketing, name="nc_colonial_marketing"),
]
