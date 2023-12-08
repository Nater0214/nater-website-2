from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about-me", views.about_me, name="about_me"),
    path("about-site", views.about_site, name="about_site"),
    path("tools", views.tools, name="tools"),
    path("tools/popup-maker", views.popup_maker, name="popup_maker"),
    path("shrek-fanpage", views.shrek_fanpage, name="shrek_fanpage"),
    path("games", views.error503, name="games"),
    path("games/clicker", views.error503, name="clicker"),
    path("projects/computing-innovation", views.computing_innovation, name="computing_innovation"),
    path("user", views.user, name="user"),
]
