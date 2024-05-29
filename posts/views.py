from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from posts.models import Post
from posts.forms import PostCreationForm, PostUpdationForm
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
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form_obj = form.save(commit=False)
            form_obj.author = request.user
            form_obj.save()
            return redirect(reverse("homepage"))

    context = {"form": form}
    return render(request, "posts/createpost.html", context)




# Implemntation of Django Generic Class Based View for CRUD Operations

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class PostsListView(ListView):
    model = Post
    queryset = Post.objects.order_by('title')[:100]
    template_name = 'posts/posts_list_view.html'
    context_object_name = 'posts_list'


class PostsDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail_view.html'
    context_object_name = 'post'


class PostCreationView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'posts/post_create_view.html'
    success_url = reverse_lazy('post_created')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)
    

class PostUpdationView(UpdateView):
    model = Post
    form_class = PostUpdationForm
    template_name = 'posts/post_update_view.html'
    success_url = reverse_lazy('post_updated')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete_view.html'
    success_url = reverse_lazy('post_deleted')


def post_created(request):
    return HttpResponse('<h1>Post Created</h1>')


def post_updated(request):
    return HttpResponse('<h1>Post Updated</h1>')


def post_deleted(request):
    return HttpResponse('<h1>Post deleted</h1>')
