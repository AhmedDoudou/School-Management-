from django.contrib import admin
from .models import *

admin.site.register(Inscription)
admin.site.register(Membership)
admin.site.register(Parent)
admin.site.register(Program)
admin.site.register(Payment)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","last_name", "first_name")


