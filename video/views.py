from django.shortcuts import render
from .models import video

# Create your views here.
def index(request):
	Video=video.objects.all()
	return render(request,"index.html",{"video":Video})

