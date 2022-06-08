from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    
class PostDetail(DetailView):
    model = Post
    
from django.shortcuts import render
def chartTest (request):
    
    posts = Post.objects.all().order_by('-pk') # 역순 정렬
    
    mylist = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7]
    myArray = ','.join([str(i) for i in mylist])
    
    return render(
        request,
        'blog/chartTest.html',
        { 'myArrays': myArray ,
          'post':posts[0], }
        
    )
    