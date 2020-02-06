from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def home(request):
    abouts = about.objects.all()
    aboutDetails = aboutinfo.objects.all()
    context = {'abouts' : abouts, 'aboutDetails': aboutDetails }
    return render(request, 'blog/home.html', context)

def about_home(request):
    abouts = about.objects.all()
    social = soicalMedia.objects.all()
    context = {'abouts' : abouts, 'social': social }
    return render(request, 'blog/base.html', context)

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = { 'post':post }
    return render (request, 'blog/post_details.html', stuff_for_frontend)
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_new.html', stuff_for_frontend)
@login_required
def post_draft(request):
    posts = Post.objects.filter(publish_date__isnull=True).order_by('-created_date')
    stuff_for_frontend = {'posts': posts }
    return render(request, 'blog/post_drafts.html',  stuff_for_frontend)
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_details', pk=pk)
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':

        # updating an existing form
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_new.html', stuff_for_frontend)
@login_required
def post_delete(request, pk):
     post = get_object_or_404(Post, pk=pk)
     post.delete()
     return redirect('/', pk=post.pk)

def contact(request):
    if request.method == 'POST':
        name =request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        message =request.POST['message']
        if len(name)<6 or len(phone)<11 or len(email)<6 or len(message)<10:
            messages.error(request, "Please, fill up the form correctly,you missed something")
        else:
            messages.success(request, " thank you ! Your message has been sent successfully. we will contact with you soon ")
        contact = Contact( name=name, email=email, message=message, phone=phone)
        contact.save()
    return render(request, 'blog/contact.html')
