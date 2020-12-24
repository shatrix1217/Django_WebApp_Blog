from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Watabe',
        'title' : 'Dummy post 1',
        'content' : 'first post content',
        'date_posted' : 'Dec 25, 2020'
    },
    {
        'author' : 'Watabe',
        'title' : 'Dummy post 2',
        'content' : 'second post content',
        'date_posted' : 'Dec 25, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html')
    
#blog -> templates -> blog -> template.html