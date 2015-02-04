from django.db import models

# Create your models here

class User(models.Model):
  uid = models.CharField('Username', max_length=20)
  pwd = models.CharField('Password', max_length=200)
  created = models.DateTimeField()
  fullname = models.CharField('Full name of user', max_length=200)
  def __str__(self):
    return self.uid


class Role(models.Model):
  rolename = models.CharField(max_length=20)
  created = models.DateTimeField()
  def __str__(self):
    return self.rolename


class RoleMap(models.Model):
  user = models.ForeignKey(User)
  roles = models.ManyToManyField(Role)
