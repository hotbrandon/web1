from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('eggs are great')

def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wlist = fulltext.split()

    mydict = {}
    for word in wlist:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] =1
    sorted_list = sorted(mydict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext' : fulltext, 'count' : len(wlist), 'mydict' : sorted_list})
