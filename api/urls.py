from django.urls import path

from .views import UsersApiView ,UserDetailView , ArticlesApiView ,ArticleDetailView

urlpatterns =[
    path("",ArticlesApiView.as_view()),
    path("<int:pk>/", ArticleDetailView.as_view()),
    path("users/",UsersApiView.as_view()),
     path("users/<int:pk>/", UserDetailView.as_view()),
]