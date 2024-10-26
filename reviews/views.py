from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerialiser
    permission_classes =[permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerialiser
    permission_classes=[permissions.IsAuthenticated]
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialiser
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerialiser
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialiser
    filter_backends= [DjangoFilterBackend]
    filterset_fields = ['slug']
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
    
    
    
    
