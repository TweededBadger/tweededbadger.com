from django.shortcuts import render,get_object_or_404

def index(request):
    return render(request,'about/index.html')

def tools(request):
    return render(request,'about/tools.html')