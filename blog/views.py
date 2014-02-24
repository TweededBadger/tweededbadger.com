from django.shortcuts import render,get_object_or_404
from blog.models import Post,Image

def index(request):
    posts = Post.objects.filter(published=True)
    return render(request,'blog/index.html',{'posts':posts})
def images(request):
    images = Image.objects.all()
    return  render(request,'blog/images.html',{'images':images})
def post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,'blog/post.html',{'post':post})