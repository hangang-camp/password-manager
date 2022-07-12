from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class UserOwnAccount(models.Model):
    alias = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sitename = models.CharField(max_length=255)
    siteurl = models.CharField(max_length=255)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='own_account')


class Tag(models.Model):
    name = models.CharField(max_length=255)


class AccountTagMap(models.Model):
    tag_id = models.ForeignKey(
        Tag, on_delete=models.CASCADE, related_name='account_map')
    account_id = models.ForeignKey(
        UserOwnAccount, on_delete=models.CASCADE, related_name='tag_map_account')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tag_map_user')
