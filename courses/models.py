from django.db import models

# Create your models here.

class CourseCategory(models.TextChoices):
       
       SCHOOLS = "schools", "Schools"
       UG_PG = "ug-pg", "UG / PG"
       CERTIFICATION = "certification", "Certification"
       PROFESSIONAL = "professional", "Professional"
       SPECIALIZED = "specialized", "Specialized"

class Course(models.Model):
       title = models.CharField(max_length=200)
       category = models.CharField(max_length=20, choices=CourseCategory.choices)
       description = models.TextField()
       syllabus = models.JSONField(default=list, blank=True)
       is_active = models.BooleanField(default=True)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
       
       class Meta:
              ordering = ["-created_at"]
       
       def __str__(self):
              return f"{self.category} = {self.title}"


       
class CourseApplication(models.Model):
       name = models.CharField(max_length=150)
       phone = models.CharField(max_length=20)
       email = models.EmailField()
       course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL, related_name="applications")
       category = models.CharField(max_length=20, choices=CourseCategory.choices, blank=True)
       message = models.TextField(blank=True)
       created_at = models.DateTimeField(auto_now_add=True)
       is_reviewed = models.BooleanField(default=False)

       class Meta:
              ordering = ["-created_at"]
              
       
       def __str__(self):
              return f"{self.name} - {self.course.title if self.course else self.category}"

