from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, SignupSerializer, LoginSerializer

User = get_user_model()

class SignupView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = SignupSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        
        try:
            user = serializer.save() 
        except Exception as e:
            return Response({"error at signup": str(e)}, status = status.HTTP_400_BAD_REQUEST)
        
        django_login(request, user)  # Log the user in after successful signup
        return Response(UserSerializer(user).data, status = status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        data = serializer.validated_data 
        
        user = authenticate(request, username = data["uid"], password = data["password"])
        
        if user is None:
            return Response({"error at login": "Invalid credentials"}, status = status.HTTP_401_UNAUTHORIZED)
        
        django_login(request, user)  # Log the user in after successful authentication
        return Response(UserSerializer(user).data, status = status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        django_logout(request) # Log the user out
        return Response({"message": "Logged out successfully"}, status = status.HTTP_200_OK)


# if Front-end refrash page, it will call [GET: auth/me] to check if the user is logged-in or not. 
# If logged-in, it will return the user data to the Front-end. 

@method_decorator(ensure_csrf_cookie, name = "get")
class MeView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        if request.user.is_authenticated:
            return Response(UserSerializer(request.user).data, status = status.HTTP_200_OK)
        else:
            return Response({"error": "User is not authenticated"}, status = status.HTTP_401_UNAUTHORIZED)
