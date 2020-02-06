from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class about(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='aboutpics', blank=True)

    def __str__(self):
        return self.name

class aboutinfo(models.Model):
    heading = models.CharField(max_length=500)
    headingtitle = models.CharField(max_length=500)
    text = RichTextUploadingField()

    def __str__(self):
        return self.heading

class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=20)
    message = models.TextField()
    sentTime =models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name
