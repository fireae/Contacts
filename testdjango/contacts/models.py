from django.db import models

# Create your models here.

class Account(models.Model):
    account_id = models.AutoField(primary_key=True, unique=True)
    #account_id = models.IntegerField(primary_key=True, unique=True)
    account_name = models.CharField(max_length=50,unique=True)
    account_pwd = models.CharField(max_length=100)

class UserInfo(models.Model):
    account_id = models.ForeignKey(Account);
    user_id = models.AutoField(primary_key=True, unique=True)
    #user_id = models.IntegerField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=50)
    user_sex = models.IntegerField()
    user_birthday = models.DateField()
    user_horbbit = models.CharField(max_length=200)

class UserRelation(models.Model):
    user_id1 = models.IntegerField(primary_key=True)
    user_id2 = models.IntegerField(primary_key=True)
    user_remark_name = models.CharField(max_length=200)
    user_relation_status = models.IntegerField(default=0)

class Resource(models.Model):
    user_id = models.ForeignKey(UserInfo)
    resource_value = models.CharField(max_length=200)
    resource_type = models.IntegerField(default=0)

class UserWords(models.Model):
    user_id = models.ForeignKey(UserInfo)
    user_words_id = models.AutoField(primary_key=True, unique=True)
    user_words_content = models.CharField(max_length=200)
    user_words_pubdate = models.DateTimeField(auto_now=True)
    user_words_location = models.CharField(max_length=100)
