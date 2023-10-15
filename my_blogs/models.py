from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
# model for tag objcts
class Tag(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


# model for author objects
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


# model for post objects
class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to="posts_images")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    excerpt = models.CharField(max_length=255)
    content = models.TextField(validators=[MinLengthValidator(50)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


# model for comment objects
class Comment(models.Model):
    comment = models.TextField(validators=[MinLengthValidator(5)], max_length=900)
    user = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
