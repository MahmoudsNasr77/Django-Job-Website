from django.urls import include, path
from . import views
from .import api
app_name='accounts'
urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
  
    path('profile/edit',views.profile_edit,name='profile_edit'),
     path('api/list',api.profile_list_api,name='profile_list_api'),
    
]