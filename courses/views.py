from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from .models import Course, CourseApplication
from .serializers import CourseSerializers, CourseApplicationSerializers

class CourseFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category")
    search = filters.CharFilter(method="filter_search")
    
    class Meta:
        model = Course
        fields = ["category"]
    
    def filter_search(self, queryset, name, value):
        return queryset.filter(title__icontains = value)

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.filter(is_active = True)
    serializer_class = CourseSerializers
    filterset_class = CourseFilter
    permission_classes = [permissions.AllowAny]

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.filter(is_active = True)
    serializer_class = CourseSerializers
    permission_classes = [permissions.AllowAny]

class CourseApplicationCreateView(generics.CreateAPIView):
    queryset = CourseApplication.objects.all()
    serializer_class = CourseApplicationSerializers
    permission_classes = [permissions.AllowAny]


