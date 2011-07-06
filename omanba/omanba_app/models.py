
from django.db import models
from django.contrib import admin



class Article(models.Model):
	title= models.CharField(max_length=200)
	headline=models.CharField(max_length=300)
	date_created=models.DateTimeField('date published')

	ARTICLE_CHOICES=(('news', 'News'), ('lifestyle', 'Lifestyle'), ('politics', 'Politics'), ('extras', 'Extras'), ('sports', 'Sports'),)
	article_type=models.CharField(max_length=6, choices=ARTICLE_CHOICES)
	def __unicode__(self):
		return self.title


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

<<<<<<< HEAD
=======




>>>>>>> 34fb685c878539a18e830eacc34a76d8712cc3a5
class ExtrasAdmin(admin.ModelAdmin):
	list_display=('extras_title','extras_headlines','extras_body')


<<<<<<< HEAD
=======
class DonateAdmin(admin.ModelAdmin):
	list_display=('project_title','project_author','project_body')

class Gh_VidAdmin(admin.ModelAdmin):
	list_display=('gh_vid_title','gh_file','gh_vid_body')


>>>>>>> 34fb685c878539a18e830eacc34a76d8712cc3a5
admin.site.register(Article)
admin.site.register(Extras)
admin.site.register(Gh_Vid)
admin.site.register(Donate)
<<<<<<< HEAD
admin.site.register(Gh_Vid,Gh_VidAdmin)
admin.site.register(Extras,ExtrasAdmin)
admin.site.register(Donate,DonateAdmin)
admin.site.register(Article)
=======
>>>>>>> 34fb685c878539a18e830eacc34a76d8712cc3a5

