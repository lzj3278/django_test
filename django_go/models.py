# coding: utf-8

from __future__ import unicode_literals

from django.db import models

import datetime


# Create your models here.

class UserInfo(models.Model):
	'''
	外键关系
	'''
	username = models.CharField(max_length=50)

	password = models.CharField(max_length=50)

	model_list = models.CharField(max_length=50)

	model_1 = models.BooleanField()
	typeId = models.ForeignKey('UserType')


class UserType(models.Model):
	name = models.CharField(max_length=30)

# model_a = models.DateTimeField()


class Group(models.Model):
	name = models.CharField(max_length=20)


class User(models.Model):
	'''
	多对多 自动创建关系表
	'''
	name = models.CharField(max_length=20)
	Email = models.CharField(max_length=20)
	Group_relation = models.ManyToManyField('Group')
# models.OneToOneField   一对一


class Asset(models.Model):
	'''
	时间自动创建
	'''
	host = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now=True)
	update_time = models.DateTimeField(auto_now=True)


class Temp(models.Model):
	'''
	简单表放内存
	'''
	GENDER_CHOICE = (
		(u'M', u'Male'),
		(u'F', u'Female'),
	)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICE)
