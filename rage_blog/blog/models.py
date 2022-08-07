from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):

    STATUS_CHOICES = (("draft", "Draft"), ("published", "Published"))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, editable=False)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="blog_posts",default='vintage_lord'
    )
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    class Meta:
        ordering = ("-updated",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # i changed "slug": self.slug to "post": self.slug because of how its referenced in comment
        return reverse("blog:post_detail", kwargs={"post": self.slug, 'pk':self.pk})

    # to get comment with parent is none and active is true, we can use this in template
    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)

# comment model    
class Comment(models.Model):

    
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name="comments")
    name=models.CharField(
        max_length=50, default='Nobody',
    )
    parent=models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)