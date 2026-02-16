from django.urls import path
from tasks.views import *

urlpatterns = [
    path("registration", regi_page, name="regi_page"),
    path("login/", login_page, name="login_page"),
    path("", home_page, name="home_page"),
    path("task-details/<str:task_id>/", task_details_page, name="task_details_page"),
    path("task-list/", task_list_page, name="task_list_page"),
    path("edit-task/<str:edit_id>/", edit_task, name="edit_task"),
    path("delete-task/<int:delete_id>/", delete_task, name="delete_task"),
    path("add-task/", add_task_page, name="add_task_page"),
    path("logout/", logout_page, name="logout_page"),
]
