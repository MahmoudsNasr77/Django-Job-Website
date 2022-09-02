from django.shortcuts import render
from job.models import Job,Category
from accounts.models import Profile
def index(request):
     job_list=Job.objects.order_by('publish_at').reverse()[:4]
     profile =Profile.objects.all()
     category=Category.objects.all()
     job_count = Job.objects.count()
     context={'job_list':job_list,'profile':profile,'category':category,'job_count':job_count}
     return render(request,'home.html',context)
