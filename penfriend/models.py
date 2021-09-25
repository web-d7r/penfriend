from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


# Create your models here.
class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    birth_date = models.DateField(null=True, blank=True)
    about_me = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.user.username

    def count_age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
