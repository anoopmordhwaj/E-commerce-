from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    all_posts = []
    posts = Blogpost.objects.all().values()
    for post in posts:
        id = post['post_id']
        tittle = post['tittle']
        date = post['pub_date']
        desc = post['heading0'] +" . "+ post['cheading0']
        thumbnail = post['thumbnail']

        all_posts = all_posts + [[id, tittle, desc, date, thumbnail]]  
        
    return render(request,'blog/index.html', {'all_posts': all_posts})

def blogpost(request, id):
    post = Blogpost.objects.get(post_id = id)
    print(post)

    return render(request,'blog/blogpost.html', {'post':post})