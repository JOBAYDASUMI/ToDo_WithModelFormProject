from django.contrib import admin

from myApp.models import *

# Register your models here.

class CustomUser_Display(admin.ModelAdmin):
    list_display=["username","email","password","profile_pic"]
    search_fields=["username","email","password","profile_pic"]

    fieldsets=[
        (
            "This is my Title",
            {
                "fields":["username","email","password"]
            }
        ),
        (
            "Advance Options",
            {
                "classes":["collapse"],
                "fields":["first_name","last_name","usertype","profile_pic"]
            }
        ),
    ]

admin.site.register(CustomUser,CustomUser_Display)



admin.site.register(CategoryModel)
admin.site.register(TaskModel)
