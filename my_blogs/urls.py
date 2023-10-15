from django.urls import path

from . import views

# url paths
urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("all-posts/", views.posts, name="all-posts"),
    path("all-posts/<slug:slug>", views.post_detail, name="post-detail"),
]
