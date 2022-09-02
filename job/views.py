from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Job
from django.urls import reverse
from .form import Applyfrom,Addjob
from django.contrib.auth.decorators import login_required    
from .filters import JobFilter

def job_list(request) :
    job_list=Job.objects.all()
    job_count = Job.objects.count()
    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    context={'jobs':page_obj,'myfilter':myfilter,'job_count':job_count}
    return render (request,"job/job_list.html",context)
def job_details(request,slug):
    job_details=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=Applyfrom(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_details
            myform.save()
            return redirect(reverse('jobs:job_list'))
           
    else:
        form=Applyfrom()   
    
    context={'job':job_details,'form':form}
    return render(request,'job/job_detials.html',context)
@login_required
def add_job(request):
    if request.method=='POST':
      Job_form=Addjob(request.POST,request.FILES)
      if Job_form.is_valid():
            myform=Job_form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        Job_form=Addjob()   
    return render(request,'job/add_jobs.html',{'Job_form':Job_form})

def upload(request):
    if request.method=='POST':
        form=Applyfrom(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_details
            myform.save()
            return redirect(reverse('jobs:job_list'))
           
    else:
        form=Applyfrom()   
    
    context={'form':form}
    return render(request,'job/upload.html',context)
    