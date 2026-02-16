from django.shortcuts import render, redirect
from tasks.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def regi_page(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            UserAuthInfoModel.objects.create_user(
                full_name=full_name,
                username=username,
                email=email,
                password=password,
            )
            return redirect("login_page")
    return render(request, "registration.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home_page")
        else:
            print("wrong")
    return render(request, "login.html")


# @login_required
def home_page(request):
    data = ToDoModel.objects.filter(status="Completed")

    data_pack = {"item": data}
    return render(request, "home.html", data_pack)


def task_list_page(request):
    data = ToDoModel.objects.all()
    data_pack = {"item": data}
    return render(request, "task_list.html", data_pack)


def task_details_page(request, task_id):

    data = ToDoModel.objects.get(id=task_id)
    data_pack = {"item": data}
    return render(request, "task_details.html", data_pack)


def add_task_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")

        ToDoModel.objects.create(
            title=title, status=status, description=description, deadline=deadline
        )
        return redirect("task_list_page")
    return render(request, "add_task.html")


def logout_page(request):
    logout(request)
    return redirect("home_page")


def edit_task(request, edit_id):
    edited_task=ToDoModel.objects.get(id=edit_id)
    dataPack ={
        'task':edited_task
    }
    if request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        ToDoModel(
            id=edit_id, title=title, status=status, description=description, deadline=deadline
        ).save()
        return redirect("task_list_page")
    return render(request, "edit_task.html", dataPack)


def delete_task(req, delete_id):
    ToDoModel.objects.get(id=delete_id).delete()
    return redirect("task_list_page")
