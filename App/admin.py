from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from .models import *

class User_admin(ModelAdmin):
    def get_sex(self):
        if self.sex:
            return '男'
        else:
            return '女'
    get_sex.short_description = '性别'
    list_display = ['name', 'age', get_sex, 'birth']

admin.site.register(Users, User_admin)