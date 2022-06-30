from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\221?\d{9,10}$')], max_length=10, blank=True)
    address = models.CharField(max_length=32, blank=True)
    profession = models.CharField(max_length=32, blank=True)
    age = models.IntegerField(blank=True)
    sex = models.CharField(max_length=8, blank=True)
    relative = models.ManyToManyField('Relatives', related_name='profiles')

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])


class Relatives(models.Model):
    son = 'Son'
    daughter = 'Daughter'
    brother = 'Brother'
    sister = 'Sister'
    mother = 'Mother'


    choice_link = [
        (son, 'Son'),
        (daughter, 'Daughter'),
        (brother, 'Brother'),
        (sister, 'Sister'),
        (mother, 'Mother'),

    ]
    link = models.CharField(max_length=32, blank=False, choices=choice_link) # if he(she) is a son, daughter, bro or sis...
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    phone = models.CharField(validators=[RegexValidator(regex=r'^\221?\d{9,10}$')], max_length=10, blank=True)
    email = models.EmailField(max_length=64, blank=True)
    address = models.CharField(max_length=32, blank=True)
    profession = models.CharField(max_length=32, blank=True)
    age = models.IntegerField(blank=True)
    sex = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.link}"



