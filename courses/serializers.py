from rest_framework import serializers
from .models import CourseCategory, Course, CourseApplication

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "title", "category", "description", "syllabus"]

class CourseApplicationSerializers(serializers.ModelSerializer):
    
    courseId = serializers.CharField(write_only = True, required = True)
    
    class Meta:
        model = CourseApplication
        firlds = ["id", "name", "phone", "email", "courseId", "message", "created_at"]
        read_only_fields = ["id", "created_at"]
    
        def validate(self, attrs):
            raw = attrs.pop("courseId")
            # If choice is number by any chance: it will set courseId as FK
            if raw.isdigit():
                try:
                    attrs["course"] = Course.objects.get(pk = int(raw))
                except Course.DoesNotExist:
                    raise serializers.ValidationError({"courseId": "This course no longer exists."})
            # If choice is string it's check with category values and create a category field and value in attrs.
            elif raw in CourseCategory.values: attrs["category"] = raw
            else: raise serializers.ValidationError({"courseId": "Unrecognized course or category."})
            
            return attrs
        
        