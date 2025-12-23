from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'full_name', 'department')
    search_fields = ('student_id', 'full_name')
    list_filter = ('department',)
