from django.urls import include, path
from . import views
app_name='home'
urlpatterns = [
    path('',views.index,name='index'),

    
]