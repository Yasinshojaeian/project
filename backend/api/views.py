from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .permissions import IsSuperUser, IsSuperUserOrStaffReadOnly
from .permissions import IsStaffOrReadOnly , IsAuthorOrReadOnly
from rest_framework.generics import RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from blog.models import Article
from .serializers import ArticleSerialiser , UserSerialiser , AuthorSerialiser
from django.contrib.auth.models import User
class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerialiser
    filter_fields = ["status", "author"]
    search_fields = ["title" ,"content","author__username","author__first_name","author__last_name"]
    ordering = ["-publish"]
    ordering_fields = ["status", "publish"]

    def get_permission(self):
        if self.action in ['list','create']:
            permissions_class = [IsStaffOrReadOnly] 
        else :
            permissions_class =[IsStaffOrReadOnly,IsAuthorOrReadOnly]
        return [permission() for permission in permissions_class]

class UserViewSet(ModelViewSet):
    queryset =get_user_model().objects.all()
    serializer_class = UserSerialiser
    permission_classes = [IsSuperUserOrStaffReadOnly]

class AuthorRetrieve(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = AuthorSerialiser
    