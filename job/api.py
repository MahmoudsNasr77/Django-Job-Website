from .models import Job
from rest_framework.decorators import api_view
from .serializers import jobSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
@api_view(['GET'])
def job_list_api(request):
    all_job=Job.objects.all()
    data=jobSerializer(all_job,many=True).data
    return Response({'data':data})
@api_view(['GET'])
def job_details_api(request,id):
    job_dtails=Job.objects.get(id=id)
    data=jobSerializer(job_dtails).data
    return Response({'data':data})

class JobListApi(generics.ListAPIView):
    queryset=Job.objects.all()
    serializer_class =jobSerializer
class JobDetailsApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =jobSerializer
    queryset=Job.objects.all()
    lookup_field = 'id'
    