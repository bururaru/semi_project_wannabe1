from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


# class UserRegister2(models.Model) :
#     user_id = models.CharField(max_length=50)
#     user_pwd= models.CharField(max_length=50)
#     user_email= models.CharField(max_length=50)

#     bio = models.TextField(max_length=500, blank=True)
#     contact = models.CharField(max_length=50, blank=True)
#     location = models.CharField(max_length=30, blank=True)

#     profile_img= models.ImageField(null=True)

#     def __str__(self):
#         return self.user_id+", "+self.user_pwd+", "+self.user_email


class StuProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20, blank=True)
    user_pwd = models.CharField(max_length=20, blank=True)
    user_email = models.CharField(max_length=20, blank=True)

    bio = models.TextField(max_length=500, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=30, blank=True)
    # profile_img= models.ImageField(null=True)

    def __str__(self):
        return self.user_name

@receiver(post_save, sender=User)
def create_user_stuprofile(sender, instance, created, **kwargs):
    if created:
        StuProfile.objects.create(user=instance, user_name = instance.username)
        # bio = instance.bio, contact = instance.contact, location = instance.location, profile_img = instance.profile_img


@receiver(post_save, sender=User)
def save_user_stuprofile(sender, instance, **kwargs):
    instance.stuprofile.save()

