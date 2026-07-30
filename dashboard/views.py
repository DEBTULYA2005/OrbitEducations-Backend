from django.http import FileResponse, Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Certificate
from .serializers import CertificateSerializer, ProfileSerializer


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(ProfileSerializer(request.user).data)

    def patch(self, request):
        serializer = ProfileSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CertificateListView(generics.ListAPIView):
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Certificate.objects.filter(user=self.request.user)


class CertificateDownloadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            certificate = Certificate.objects.get(pk=pk, user=request.user)
        except Certificate.DoesNotExist:
            raise Http404

        return FileResponse(
            certificate.file.open("rb"),
            as_attachment=True,
            filename=f"{certificate.title}.pdf",
        )