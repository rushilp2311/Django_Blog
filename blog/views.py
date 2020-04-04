from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author':'Rushil',
        'title':'Blog Post_1',
        'content':'First post content',
        'date_posted':'August 27,2018'
    },
    {
        'author':'Patel',
        'title':'Blog Post_2',
        'content':'Second post content',
        'date_posted':'August 28,2018'
    }
]
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
