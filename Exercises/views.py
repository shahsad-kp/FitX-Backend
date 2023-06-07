from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from Exercises.models import Category
from Exercises.serializers import CategorySerializer


