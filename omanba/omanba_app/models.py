
from django.db import models
from django.contrib import admin



class Article(models.Model):
	title= models.CharField(max_length=200)
	headline=models.CharField(max_length=300)
	date_created=models.DateTimeField('date published')
<<<<<<< HEAD
	ARTICLE_CHOICES=(('news', 'News'), ('lifestyle', 'Lifestyle'), ('politics', 'Politics'), ('extras', 'Extras'), ('sports', 'Sports'),)
	article_type=models.CharField(max_length=6, choices=ARTICLE_CHOICES)
	def __unicode__(self):
		return self.title


=======
	STATUS_CHOICES=(('news', 'News'), ('lifestyle', 'Lifestyle'), ('politics', 'Politics'), ('extras', 'Extras'), ('sports', 'Sports'),)
	article_type=models.CharField(max_length=6, choices=STATUS_CHOICES)
	def __unicode__(self):
		return self.title

>>>>>>> 4d5a6750f01f5e8d8c6bf79983c87bf40cb48df8

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

class ExtrasAdmin(admin.ModelAdmin):
	list_display=('extras_title','extras_headlines','extras_body')


admin.site.register(Article)
admin.site.register(Extras)
admin.site.register(Gh_Vid)
admin.site.register(Donate)
admin.site.register(Gh_Vid,Gh_VidAdmin)
admin.site.register(Extras,ExtrasAdmin)
admin.site.register(Donate,DonateAdmin)
admin.site.register(Article)

