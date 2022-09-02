from django.urls import include, path
from .import views
from .import api
app_name='job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
     path('add',views.add_job,name='add_jobs'),
     path('upload',views.upload,name='upload'),
    path('<str:slug>',views.job_details,name='job_details'),
    
   path('api/job',api.job_list_api,name='job_list_api'),
   path('api/job/<int:id>',api.job_details_api,name='job_details_api'),
    
   path('api/v2/job',api.JobListApi.as_view(),name='JobListApi'),
      path('api/v2/job/<int:id>',api.JobDetailsApi.as_view(),name='JobDetailsApi'),

]