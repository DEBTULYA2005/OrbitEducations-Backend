from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from courses.models import Course, CourseApplication, CourseCategory

User = get_user_model()

# Authenticate user loged-in in Front-end and return the user data to the Front-end.
class UserSerializer(serializers.ModelSerializer):
    
    parentName = serializers.CharField(source = "parent_name", required = False, allow_blank = True)
    parentPhone = serializers.CharField(source = "parent_phone", required = False, allow_blank = True)
    enrolledCourse = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            "uid", "name", "email", "phone", "parentName", "parentPhone", 
            "address", "enrolledCourse", "date_joined",
        ]
        # Fields cannot be modified from the front-end.
        read_only_fields = ["uid", "enrolledCourse", "date_joined"]
        
    def get_enrolledCourse(self, obj):
        if obj.enrolled_course: return obj.enrolled_course.title
        else: return None

class SignupSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only = True, required = True, validators = [validate_password])
    parentName = serializers.CharField(source = "parent_name", required = False, allow_blank = True)
    parentPhone = serializers.CharField(source = "parent_phone", required = False, allow_blank = True)
    enrolledCourse = serializers.CharField(write_only = True, required = False, allow_blank = True)
    
    class Meta:
        model = User
        fields = [
            "uid", "name", "email", "phone", "password", "parentName", "parentPhone", "address", "enrolledCourse",
        ]
        
    def validate_uid(self, value):
        if User.objects.filter(uid = value).exists():
            raise serializers.ValidationError("A user with this UID already exists.")
        return value
    
    def validate_enrolledCourse(self, value):
        if value and value not in CourseCategory.values: 
            raise serializers.ValidationError("Unrecognized course category.")
        return value
    
    def create(self, validated_data):
        category = validated_data.pop("enrolledCourse", "")
        password = validated_data.pop("password")  # Remove password from validated_data to avoid storing it in plain text
        
        course = None
        if category:
            course = Course.objects.filter(category=category, is_active=True).first()

        user = User(**validated_data, enrolled_course=course)  
        user.set_password(password)
        user.save()  # Save the user instance to the database
        return user

class LoginSerializer(serializers.Serializer):
    
    uid = serializers.CharField()
    course = serializers.CharField(required = False, allow_blank = True)
    password = serializers.CharField(write_only = True)


    