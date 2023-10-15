from django.contrib import auth
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import CommentForm
from .models import Post

# variables
all_posts = Post.objects.all().order_by("-date")


# Create your views here.
# view route for home page
def index(request):
    latest_posts = all_posts[:3]

    return render(
        request,
        "my_blogs/index.html",
        {
            "posts": latest_posts,
        },
    )


# view route for about page
def about(request):
    return render(
        request,
        "my_blogs/about.html",
    )


# view route for all posts route
def posts(request):
    return render(
        request,
        "my_blogs/all-posts.html",
        {
            "posts": all_posts,
        },
    )


# view route for post's detail
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = auth.get_user(request)
            comment.save()

            return redirect(reverse("post-detail", args=[slug]))

    return render(
        request,
        "my_blogs/post-detail.html",
        {
            "post": post,
            "tags": post.tags.all(),
            "form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
        },
    )
