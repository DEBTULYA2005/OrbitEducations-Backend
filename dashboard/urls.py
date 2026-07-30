from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/profile/", views.ProfileView.as_view(), name="dashboard-profile"),
    path("dashboard/certificates/", views.CertificateListView.as_view(), name="dashboard-certificates"),
    path(
        "dashboard/certificates/<int:pk>/download/",
        views.CertificateDownloadView.as_view(),
        name="dashboard-certificate-download",
    ),
]