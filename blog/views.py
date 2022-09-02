from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import blog,comment
from django.urls import reverse
from .forms import CommentForm,BlogForm
from django.contrib.auth.decorators import login_required    
from .filters import postFilter
from accounts.models import Profile
def blog_list(request):  
    blog_list=blog.objects.order_by('title')
    myfilter=postFilter(request.GET,queryset=blog_list)
    blog_list=myfilter.qs
    paginator = Paginator(blog_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    context={'blog':page_obj,'myfilter':myfilter}
    return render(request,"blog.html",context)
@login_required
def add_post(request):
    if request.method=='POST':
      blog_form=BlogForm(request.POST,request.FILES)
      if blog_form.is_valid():
            myform=blog_form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect(reverse('blog:blog_list'))
    else:
        blog_form=BlogForm()   
    return render(request,'add_blog.html',{'blog_form':blog_form})
@login_required
def blog_details(request,slug):
    blog_details=blog.objects.get(slug=slug)
    comment_count=comment.objects.count()
    recent_post=blog.objects.order_by("publish_at").reverse()[:3] 
    reply=comment.objects.all()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.blog=blog_details
            myform.save()
            return redirect(request.META['HTTP_REFERER'])
           
    else:
        form=CommentForm()   
    context={'blog_details':blog_details,'blog':CommentForm,'form':form,'comment_count':comment_count,'reply':reply,'recent_post':recent_post}
    return render(request,'blog_details.html',context)


 
