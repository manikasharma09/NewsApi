from django.shortcuts import render
from newsapi import NewsApiClient

def index(request):
	newsapi=NewsApiClient(api_key='6978d2057e684c708b85fe09b24be6a7')
	top=newsapi.get_top_headlines(sources='bbc-news')

	l=top['articles']
	news=[]
	img=[]
	desc=[]

	for i in range(len(l)):
		f=l[i]
		news.append(f['title'])
		img.append(f['urlToImage'])
		desc.append(f['description'])
		mylist=zip(news,desc,img)

		return render(request,'index.html',context={"mylist":mylist})
