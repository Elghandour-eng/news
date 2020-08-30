from rest_framework import serializers
from django.contrib.auth.models import User
from articles.models import Article
from users.models import CustomUser

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model =Article
        fields=('title','body','author')

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =CustomUser
        fields=('id','username',"email",'age','password')