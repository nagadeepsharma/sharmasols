from django.shortcuts import render
from .models import Pp,Content

# Create your views here.
def index(request):
    p=Pp.objects.all()
    data=Content.objects.all()
    return render(request,'sharma/index.html',{'p':p,'data':data})
