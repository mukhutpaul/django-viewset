from rest_framework import serializers
from django.contrib.auth.models import User,Group
from .models import *

class UserSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']
        
class GroupSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','name']
        
class ReviewSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
class BusinessSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"

class CategorySerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        depth = 1
        fields = "__all__"