from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.published)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):

    class Status(models.TextChoices):# tanlash hosil qilish uchun ishlatiladi dropdown
        draft = "DF","Draft"
        published = "PD","Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)# yanglik qachonki saytga chiqarilsa o'sha vaqtni oladi
    created_time = models.DateTimeField(auto_now_add=True) #yaratilgan vaqtni avtomatik oladi va bu vaqtni o'zgartrib bolmaydi
    updated_time = models.DateTimeField(auto_now=True)#har safar yangilanganda yangi vaqtni oladi ,o'zgartirsa boladi
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.draft
                              )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-publish_time"] #yangliklarni teskari tartiblab chiqarish, yani oxirgi qo'shilgan birinchida


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail',args=[self.slug])



class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email


class Fotografiya(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news/fotografiya')
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




