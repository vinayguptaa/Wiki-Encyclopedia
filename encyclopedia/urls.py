from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    path("show/<str:name>",views.show_page,name="show_page"),
    path("search",views.search,name="search"),
    path("new_page",views.new_page,name="new_page"),
    path("adding",views.adding,name="adding"),
    path("editing",views.editing,name="editing"),
    path("edit/<str:entry>",views.edit_entry,name="edit_entry"),
    path("show/edit/<str:entry>",views.edit_entry,name="edit_entry"),
    path("random_page",views.random_page,name="random_page"),
]
