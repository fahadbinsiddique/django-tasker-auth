from django.shortcuts import render, redirect
from tasks.models import *
from django.contrib.auth import authenticate, login


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


def home_page(request):
    data = ToDoModel.objects.filter(status="Completed")
    print('erer',data)
    data_pack = {"item": data}
    print('fff',data_pack)
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
        ToDoModel.objects.create(title=title, status=status, description=description)
        return redirect("task_list_page")
    return render(request, "add_task.html")
