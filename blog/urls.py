from django.urls import include, path
from . import views
app_name='blog'
urlpatterns = [
    path('',views.blog_list,name='blog_list'),
    path('add',views.add_post,name='add_post'),
    path('<str:slug>',views.blog_details,name='blog_details'),
    
      
   
    

   
    
]