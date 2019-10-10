from django.shortcuts import render
from django.http import JsonResponse
from newsapi import NewsApiClient
import json

NEWS_API_KEY='6978d2057e684c708b85fe09b24be6a7'

def index(request):
	return render(request, 'index.html')

def news(request):
	newsapi=NewsApiClient(api_key=NEWS_API_KEY)
	top=newsapi.get_top_headlines(sources='bbc-news')

	l=top['articles']
	newsDict={}
	c=0
	for i in range(len(l)):
		f=l[i]
		newsDict[c]={
			'title':f['title'],
			'urlToImage':f['urlToImage'],
			'description':f['description']
		}
		c+=1

	return JsonResponse({'news':json.dumps(newsDict), 'status':'200'})
