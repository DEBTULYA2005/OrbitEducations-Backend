from django.urls import path
from . import views

urlpatterns = [
    path("notifications/", views.NotificationListView.as_view(), name="notification-list"),
    path("notifications/mark-all-read/", views.NotificationMarkAllReadView.as_view(), name="notification-mark-all-read"),
    path("notifications/<int:pk>/", views.NotificationUpdateView.as_view(), name="notification-update"),
]