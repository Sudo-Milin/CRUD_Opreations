from django.urls import path
from . import views

app_name = "crud_app"

urlpatterns = [
    path("", views.home, name="home-page"),
    path("create/", views.create, name="create-page"),
    path("list/", views.retrive_list, name="retrive-page"),
    path("update/", views.update_text, name="update-list"),
    path("update/<int:pk>/", views.update, name="update-page"),
    path("delete/", views.delete_text, name="delete-page"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]