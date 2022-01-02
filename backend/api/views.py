# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView , RetrieveUpdateDestroyAPIView , ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from blog.models import Article
from .serializers import ArticleSerialiser , UserSerialiser
from django.contrib.auth.models import User
# Create your views here.
class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    tmpArticle = Article.objects.get(id=3)
    tmpArticle.title='ali'
    tmpArticle.save()
    serializer_class = ArticleSerialiser

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsAdminUser,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialiser
    permission_classes = (IsAdminUser,)