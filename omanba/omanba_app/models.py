
from django.db import models
from django.contrib import admin

class Article(models.Model):
	title= models.CharField(max_length=200)
	headline=models.CharField(max_length=300)
	date_created=models.DateTimeField('date published')
	article_options=((news, News), (lifestyle, Lifestyle), (politics, Politics), (extras, Extras), (sports, Sports))
	article_type=models.CharField(max_length=6, choices=article_options)
	def __unicode__(self):
		return self.title

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

class Gh_Vid(models.Model):
	gh_vid_title=models.CharField(max_length=200)
	gh_vid_body=models.TextField()
	gh_file = models.FileField(upload_to='home/aiti/Desktop/')
	def __unicode__(self):
		return self.gh_vid_title
	
class Donate(models.Model):
	project_title=models.CharField(max_length=200)
	project_body=models.TextField()
	project_author=models.CharField(max_length=60)
	def __unicode__(self):
		return self.project_title

class Lifestyle(models.Model):
	lifest_title=models.CharField(max_length=200)
	lifest_body=models.TextField()
	lifest_author=models.CharField(max_length=60)
	def __unicode__(self):
		return self.lifest_title
	


class NewsAdmin(admin.ModelAdmin):
	list_display=('news_title','news_Headlines','news_body')

class SportsAdmin(admin.ModelAdmin):
	list_display=('sports_title','sports_Headlines','sports_body')

class PoliticsAdmin(admin.ModelAdmin):
	list_display=('politics_title','politics_Headlines','politics_body')

class ExtrasAdmin(admin.ModelAdmin):
	list_display=('extras_title','extras_Headlines','extras_body')

class Gh_VidAdmin(admin.ModelAdmin):
	list_display=('gh_vid_title','gh_vid_body','gh_file')

class DonateAdmin(admin.ModelAdmin):
	list_display=('project_title','project_author','project_body')

class LifestyleAdmin(admin.ModelAdmin):
	list_display=('lifest_title','lifest_author','lifest_body')

admin.site.register(News,NewsAdmin)
admin.site.register(Politics,PoliticsAdmin)
admin.site.register(Gh_Vid,Gh_VidAdmin)
admin.site.register(Extras,ExtrasAdmin)
admin.site.register(Donate,DonateAdmin)
admin.site.register(Sports,SportsAdmin)
admin.site.register(Lifestyle,LifestyleAdmin)
