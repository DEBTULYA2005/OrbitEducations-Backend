from django.conf import settings
from django.db import models


class Certificate(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="certificates"
    )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="certificates/%Y/%m/")
    issued_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-issued_date"]

    def __str__(self):
        return f"{self.title} — {self.user.uid}"