from django.contrib import admin
from tasks.models import *


# Register your models here.
class AuthAdmin(admin.ModelAdmin):
    list_display = ["username", "full_name", "email"]


admin.site.register(UserAuthInfoModel, AuthAdmin)


class ToDoAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]


admin.site.register(ToDoModel, ToDoAdmin)
