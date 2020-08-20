from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')



class Article(models.Model):
    STATUS=(
        ('draft','Draft'),
        ('publish','Publish')
    )
    title=models.CharField(max_length=120)
    slug=models.SlugField(max_length=120,unique=True)
    body=RichTextUploadingField()
    publish=models.DateField(default=timezone.now)
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    status = models.CharField(max_length=20,choices=STATUS)
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    objects=models.Manager()
    published=PublishedArticleManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail',args=[self.id, self.slug])

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    reply=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    is_reply=models.BooleanField(default=False)
    body=models.TextField(max_length=400)
    created=models.DateField(auto_now_add=True)


    