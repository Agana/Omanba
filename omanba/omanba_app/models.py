from django.db import models
from django.contrib import admin

class News(models.Model):
	news_title=models.CharField(max_length=200)
	news_Headlines=models.CharField(max_length=300)
	news_date=models.DateTimeField('date published')
	news_body=models.TextField()
	def __unicode__(self):
		return self.news_title

class Sports(models.Model):
	sports_title=models.CharField(max_length=200)
	sports_Headlines=models.CharField(max_length=300)
	sports_date=models.DateTimeField('date published')
	sports_body=models.TextField()
	def __unicode__(self):
		return self.sports_title

class Politics(models.Model):
	politics_title=models.CharField(max_length=200)
	politics_Headlines=models.CharField(max_length=300)
	politics_date=models.DateTimeField('date published')
	politics_body=models.TextField()
	def __unicode__(self):
		return self.politics_title

class Extras(models.Model):
	extras_title=models.CharField(max_length=200)
	extras_headlines=models.CharField(max_length=300)
	extras_date=models.DateTimeField('date published')
	extras_body=models.TextField()
	def __unicode__(self):
		return self.extras_title

class Gh-Vid(models.Model):
	gh_vid_title=models.CharField(max_length=200)
	gh_vid_body=models.TextField()
	gh_file = models.FileField(upload_to='home/aiti/Desktop/')
	

class Donate(models.Model):
	project_title=models.CharField(max_length=200)
	project_body=models.TextField()
	project_author=models.CharField(max_length=60)

class NewsAdmin(admin.ModelAdmin):
	list_display = ('news_title','news_Headlines','news_date',)
	
admin.site.register(News)
# Create your models here.
