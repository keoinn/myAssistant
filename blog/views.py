from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>")
        # 新增以下程式碼於迴圈中
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")

    return HttpResponse(post_lists)


from datetime import datetime
def index_post(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'pages/index.html', locals())


from django.shortcuts import redirect
def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None :
            return render(request, 'pages/post.html', locals())
    except:
        return redirect('/')

