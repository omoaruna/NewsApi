from django.shortcuts import render
from .serializers import NewsSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import News
import requests

class HomePage(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class DetailsPage(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = "id"

def generate_news(request):
        if request.method == "GET":
           
            endpoint = "https://newsdata.io/api/1/news?country=ng&apikey=pub_237206c887657733da985137cc189fcffc784"
            response = requests.get(endpoint)
            news_dictionary = dict(response.json())

            for i in range(0,5):

                api_news_title = news_dictionary['results'][i]['title']
                api_news_creator = news_dictionary['results'][i]['creator']
                api_news_full_description = news_dictionary['results'][i]['description']
                api_news_source_id = news_dictionary['results'][i]['source_id']
                
                my_endpoint = "http://127.0.0.1:8000/"


                response = requests.post(my_endpoint, data={"title":api_news_title,"content":api_news_full_description,"author":api_news_creator,"source":api_news_source_id})
            return render(request,"weather.html")
        

            
            

# Create your views here.
