from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("toggle/<int:task_id>/", views.toggle_task, name="toggle_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
]
