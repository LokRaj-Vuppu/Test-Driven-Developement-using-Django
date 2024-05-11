from django.shortcuts import render, redirect
from django.urls import reverse
from posts.models import Post
from posts.forms import PostCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    try:
        posts = Post.objects.all()
        return render(request, "posts/index.html", {"posts": posts})
    except Exception as error:
        print(f"Exception in home page - {error}")


def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
        context = {"post": post, "title": post.title}
        return render(request, "posts/detail.html", context)
    except Exception as error:
        print(f"Exception in post details page - {error}")


@login_required
def create_post(request):
    form = PostCreationForm()
    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.author = request.user
            form_obj.save()
            return redirect(reverse('homepage'))
    
    context = {'form': form}
    return render(request, 'posts/createpost.html', context)
