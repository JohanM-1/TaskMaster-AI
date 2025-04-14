from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.list_projects, name="list_projects"),
    path("projects/create/", views.crear_projecto, name="crear_projecto"),
    path("projects/<int:project_id>/", views.view_project, name="view_project"),
    path("projects/<int:project_id>/edit/", views.edit_project, name="edit_project"),
]
