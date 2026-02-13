from django.urls import path
from tasks.views import *

urlpatterns = [
    path("", regi_page, name="regi_page"),
    path("login/", login_page, name="login_page"),
    path("home/", home_page, name="home_page"),
    path("task-details/<str:task_id>/", task_details_page, name="task_details_page"),
    path("task-list/", task_list_page, name="task_list_page"),
    path("add-task/", add_task_page, name="add_task_page"),
    path("logout/", logout_page, name="logout_page"),
]
