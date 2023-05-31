from django.urls import path
from .views import HomePage,DetailsPage,generate_news

urlpatterns = [
    path("",HomePage.as_view(),name="home"),
    path("<int:id>/",DetailsPage.as_view(),name="details"),
    path("generate_news",generate_news,name="generate-news")
]
