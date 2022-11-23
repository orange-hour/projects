from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.core.validators import MinValueValidator
from django.conf import settings

# class User(models.Model):
#     username = models.CharField(max_length=120, null=False)
#     email = models.EmailField(max_length=120, null=False)
#     name = models.CharField(max_length=20, null=False)
#     born_date = models.DateField


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

class User(AbstractUser):
    GENDER_CHOICES = (('Male', '남성'), ('Female', '여성'))
    objects = UserManager()
    
    # blank=True: 폼(입력양식)에서 빈채로 저장되는 것을 허용, DB에는 ''로 저장
    # CharField 및 TextField는 blank=True만 허용, null=True 허용 X
    nickname = models.CharField(blank=True, max_length=50)
    introduction = models.TextField(blank=True, max_length=200)
		# null=True: DB에 NULL로 저장
    profile_image = models.ImageField(blank=True, null=True) 
    first_name = None
    last_name = None
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(1)], null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
