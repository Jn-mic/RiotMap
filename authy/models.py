from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import Http404
import datetime as dt
#from django_google_maps import fields as map_fields


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField('profile_image/',blank=True)
    bio=models.TextField( blank=True, null=True, default='My Bio')
  # location=models.PointField()

    def __str__(self):
        return f'{self.user.username} Profile'

        #return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        print("signal activated---->>>", dir(instance))
        instance.profile.save

class Post(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField('post_image/',blank=True)
   # location=models.ForeignKey(Profile, related_name='profile',on_delete=DO_NOTHING,null=True,blank=True)
    pub_date=models.DateTimeField(auto_now_add=True)


    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_post(cls):
        post=cls.objects.all()
        return post

    @classmethod
    def search_post(cls,search_term):
        post=cls.objects.filter(post_name__icontain=search_term)
        return post

    @classmethod
    def get_by_author(cls,author):
        post=cls.objects.filter(author=author)
        return post

    @classmethod
    def today_riot(cls):
        today=dt.date.today()
        posts=cls.objects.filter(pub_date__date=today)
        return posts

    @classmethod
    def get_post(request,id):
        try:
            post=Post.objects.get(pk=id)
            return post

        except ObjectDoesNotExist:
            raise Http404()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=60,unique=True)

    class Meta:
        ordering = ["name"]

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.name


class Hotspot(models.Model):
    name= models.CharField(max_length=200)
    location = models.ForeignKey(Location, related_name='location', on_delete=models.DO_NOTHING, null=True, blank=True)
    city=models.CharField(max_length=100)
    image=models.ImageField('hotspot_image',blank=True)

    def save_hotspot(self):
        self.save()

    def delete_hotspot(self):
        self.delete()

    @classmethod
    def get_hotspot(cls):
        hotspot=cls.objects.all()
        return hotspot

    @classmethod
    def search_hotspot(cls,search_term):
       hotspot=cls.objects.filter(hotspot_name__icontain=search_term)
       return hotspot

    def __str__(self):
        return self.name

class Work(models.Model):
    name=models.CharField(max_length=50)
    
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name=models.CharField(max_length=50)
    
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Police(models.Model):
    name=models.CharField(max_length=50)
    
    address=models.CharField(max_length=30)
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.name


    

   



    




