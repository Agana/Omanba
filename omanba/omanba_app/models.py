from django.db import models
from django.contrib import admin



class Article(models.Model):
	title= models.CharField(max_length=200)
	headline=models.CharField(max_length=300)
	date_created=models.DateTimeField(auto_now=True)
	body= models.TextField()
	ARTICLE_CHOICES=(('news', 'News'), ('lifestyle', 'Lifestyle'), ('politics', 'Politics'), ('extras', 'Extras'), ('sports', 'Sports'),)
	article_type=models.CharField(max_length=60, choices=ARTICLE_CHOICES)
	article_image=models.ImageField('articleimage', upload_to='static')
	def __unicode__(self):
		return self.title

	def render_image(self):
		return self.article_image.url


#class Extras(models.Model):
#	extras_title=models.CharField(max_length=200)
#	extras_headlines=models.CharField(max_length=300)
#	extras_date=models.DateTimeField('date published')
#	extras_body=models.TextField()
#	def __unicode__(self):
#		return self.extras_title

class Gh_Vid(models.Model):
	gh_vid_title=models.CharField('videotitle', max_length=200)
	gh_vid_body=models.TextField()
	gh_file = models.FileField(upload_to='static')
	date_added=models.DateTimeField(auto_now=True)
	flvfilename = models.CharField( max_length=250, blank=True, null=True )
	def __unicode__(self):
		return self.gh_vid_title
	def render_video(self):
		return self.gh_file.url
	
class Donation(models.Model):
	project_title=models.CharField(max_length=200)
	project_body=models.TextField()
	project_author=models.CharField(max_length=60)
	date_project_added=models.DateTimeField(auto_now=True)
	donation_image=models.ImageField('articleimage', upload_to='static')
	def __unicode__(self):
		return self.project_title
	def render_donate_image(self):
		return self.donation_image.url



class ExtrasAdmin(admin.ModelAdmin):
	list_display=('extras_title','extras_headlines','extras_body')


class DonateAdmin(admin.ModelAdmin):
	list_display=('project_title','project_author','project_body')

class Gh_VidAdmin(admin.ModelAdmin):
	list_display=('gh_vid_title','gh_file','gh_vid_body')


admin.site.register(Article)
#admin.site.register(Extras)
admin.site.register(Gh_Vid)
admin.site.register(Donate)
admin.site.register(Gh_Vid,Gh_VidAdmin)
admin.site.register(Extras,ExtrasAdmin)
admin.site.register(Donate,DonateAdmin)
admin.site.register(Article)
admin.site.register(Donation)
