

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.http import HttpRequest, HttpResponse

from .models import Post
from .forms import PostForm

# Create your views here.

#gives all the job posts to the job posts page
def all_posts(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by('-created_on')
    return render(request, 'jobPosts.html', {'posts': posts, 'active': 'jobPosts'})

#supplies the home page with its needed information
def supply_home(request: HttpRequest) -> HttpResponse:
    lastFour = Post.objects.all().order_by('-created_on')[:4]
    all = Post.objects.all().order_by('-created_on')
    applied = False
    for post in Post.objects.all():
        for applicant in post.applicants.all():
            if (request.user == applicant):
                applied = True
                break
        else:
            continue
        break
    return render(request, 'home.html', {'latest': lastFour, 'posts': all, 'active': 'home', 'hasApplied': applied})

#adds applicant who applied to a specific job
def apply(request: HttpRequest, id: int) -> HttpResponse:
    post_item = Post.objects.get(id=id)
    post_item.applicants.add(request.user)
    post_item.save()
    return post_detail(request, id)

#for creating a new post using django form
def newpost(request):
    if request.method == 'GET':
        form = PostForm()
    else:  # POST
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            post = Post.objects.latest('created_on')
            post.posted_by = request.user
            post.save()
            return redirect('/jobPosts')
    return render(request, 'addPost.html', {'form':form})

#for showing post detail using django form and the post object
def post_detail(request, id: int):
    obj = Post.objects.get(id=id)
    applicants = obj.applicants.all()
    if request.method == 'GET':
        form = PostForm(instance=obj)
        form.fields['title'].disabled = True
        form.fields['description'].disabled = True
        form.fields['responsibility'].disabled = True
        form.fields['qualifications'].disabled = True
    else:
        form = PostForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('.')
    return render(request, 'postDetail.html', {'post': obj,'form':form, 'edit': False, 'applicants': applicants})

#for making the form editable and saving changes done to it
def post_edit(request, id: int):
    obj = Post.objects.get(id=id)
    if request.method == 'GET':
        form = PostForm(instance=obj)
        ret  = render(request, 'postDetail.html', {'post': obj,'form':form,'edit': True})
    else:
        obj = Post.objects.get(id=id)
        form = PostForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            form.fields['title'].disabled = True
            form.fields['description'].disabled = True
            form.fields['responsibility'].disabled = True
            form.fields['qualifications'].disabled = True
            return redirect('..')
    return ret

#for deleting a job post
def post_delete(request: HttpRequest, id: int):
    obj = Post.objects.get(id=id)
    obj.delete()
    return all_posts(request)

