from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Certificate


# Reuses the exact same field shape as /auth/me/ — the frontend's
# DashboardProfilePage form uses the same field names (parentName, parentPhone, etc.) whichever endpoint populated them.
class ProfileSerializer(UserSerializer):
    pass


class CertificateSerializer(serializers.ModelSerializer):
    issuedDate = serializers.DateField(source="issued_date")

    class Meta:
        model = Certificate
        fields = ["id", "title", "issuedDate"]