from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete= models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.username


class Post(models.Model):
    user = models.ForeignKey(Person,on_delete= models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    file_field = models.FileField(upload_to='uploads/', null=True)
    desc = models.TextField()

    def __str__(self):
        return f'{self.user}=> {self.title}'

