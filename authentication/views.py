from django.contrib.auth import get_user_model, authenticate, login, logout
from rest_framework.response import Response
from rest_framework import generics, status, permissions, filters
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()


class AuthUserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ["id", "email", "username", "fullname"]
    search_fields = ["id", "email", "username", "fullname"]
    ordering_fields = ["id", "email", "username", "fullname"]


class AuthUserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = "pk"


class UserRegisterAPIView(generics.GenericAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, requests, *args, **kwargs):
        serializer = self.serializer_class(data=requests.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(generics.GenericAPIView):
    pagination_class = None

    def get(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
