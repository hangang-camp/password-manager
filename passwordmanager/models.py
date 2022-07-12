from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.TextField()
    password = models.TextField()

    def __str__(self):
        return self.username


class UserOwnAccount(models.Model):
    alias = models.TextField()
    username = models.TextField()
    password = models.TextField()
    category = models.TextField()
    sitename = models.TextField()
    siteurl = models.TextField()
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_id_UserOwnAccount')


class AccountTagMap(models.Model):
    tag_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tag_id_AccountTagMap')
    account_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='account_id_AccountTagMap')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_id_AccountTagMap')


class Tag(models.Model):
    name = models.TextField()
