from django.contrib import admin
from .models import Course, CourseApplication
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "is_active", "created_at"]
    list_filter = ["category", "is_active"]
    search_fields = ["title", "description", "image_url"]

@admin.register(CourseApplication)
class CourseApplicationAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "course", "category", "is_reviewed", "created_at"]
    list_filter = ["is_reviewed", "category"]

