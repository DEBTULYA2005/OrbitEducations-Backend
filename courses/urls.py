from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.CourseListView.as_view(), name="course-list"),
    path("courses/applications/", views.CourseApplicationCreateView.as_view(), name="course-apply"),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(), name="course-detail"),
]