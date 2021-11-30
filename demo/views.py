from django.shortcuts import render,redirect
from .models import Videos
from .forms import VideoForm
# Create your views here.

def upload_video(request):
    
    if request.method == "POST":
    	form = VideoForm(request.POST,request.FILES)
    	if form.is_valid():
    		title = form.cleaned_data['title']
    		video = request.FILES['video']
    		reg = Videos(title=title,video=video)
    		reg.save()

    form = VideoForm()
    return render(request,'upload.html',{'form':form})


def display(request):
    
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
    
    return render(request,'videos.html',context)