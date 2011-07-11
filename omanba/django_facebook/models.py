from django.db import models
from django.contrib import admin


class FacebookProfileModel(models.Model):
	profile_name=models.CharField('Profile name', max_length=200)
	def __unicode__(self):
		return self.profile_name

admin.site.register(FacebookProfileModel)
