from rest_framework import generics
# Create your views here.
from users.models import CustomUser
from articles.models import Article
from .serializers import ArticleSerializer
from .serializers import UserSerializer


class ArticlesApiView(generics.ListAPIView):
    queryset =Article.objects.all()
    serializer_class =ArticleSerializer

class ArticleDetailView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer    




class UsersApiView(generics.ListAPIView):
    queryset =CustomUser.objects.all()
    serializer_class =UserSerializer

class UserDetailView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



