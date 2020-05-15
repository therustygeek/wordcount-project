from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html', {'HITHERE': 'THIS IS ME'})

def about(request):
	return render(request,'about.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	dic ={}
	for word in wordlist:
		if word in dic:
			#increase the count
			dic[word] +=1
		else :
			#add to the dict
			dic[word] = 1
	sortedwords = sorted(dic.items(), key = operator.itemgetter(1), reverse = True )


	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})