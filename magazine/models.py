from django.db import models
from profiles.models import UserProfile


class Magazine(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.CharField(max_length=200)
    intro_text = models.TextField()
    article = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        ordering = ['-date_created']

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=200)

    def __str__(self):
       return(self.post.title, self.nickname, self.date_created)