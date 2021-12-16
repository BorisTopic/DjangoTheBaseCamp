from django.db import models

# Create your models here.


class Post(models.Model):

    def __str__(self):
        return self.post_title

    post_title = models.CharField(max_length=35) #change max length to 35
    post_summary = models.TextField(max_length=300)
    post_image = models.CharField(max_length=500, default="https://image.freepik.com/free-vector/mountaineering-logo-"
                                                          "template_1126-55.jpg")


class Contact(models.Model):

    def __str__(self):
        return self.contact_name

    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_summary = models.TextField(max_length=1000)


class Newsletter(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=35)
    author = models.CharField(max_length=100)
    article = models.TextField(max_length=2000)
    image = models.CharField(max_length=500, default="https://image.freepik.com/free-vector/mountaineering-logo-"
                                                     "template_1126-55.jpg")