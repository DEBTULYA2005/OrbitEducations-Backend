from rest_framework import serializers
from .models import CourseCategory, Course, CourseApplication

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "category", "description", "syllabus"]

class CourseApplicationSerializers(serializers.ModelSerializer):

    courseId = serializers.PrimaryKeyRelatedField(
        source="course",
        queryset=Course.objects.filter(is_active=True),
        write_only=True
    )
    
    courseTitle = serializers.CharField(
        source="course.title",
        read_only=True
    )

    class Meta:
        model = CourseApplication
        fields = [
            "id",
            "name",
            "phone",
            "email",
            "courseId",
            "courseTitle",
            "message",
            "created_at"
        ]
        read_only_fields = ["id", "created_at", "courseTitle"]          
        
        