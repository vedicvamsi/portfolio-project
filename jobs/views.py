from django.shortcuts import render
from .models import Job
# Create your views here.
def home(request):
    jobs = Job.objects.order_by('id').reverse()
    return render(request,'jobs/home.html',{'jobs':jobs})