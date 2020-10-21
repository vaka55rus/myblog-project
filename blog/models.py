from django.db import models

class Post(models.Model):
	event_text = models.CharField(max_length=300)
	blog_date =	models.DateTimeField()
	blog_title = models.TextField()
	blog_image = models.ImageField(upload_to='blog_images/')

	def get_summary(self):
		return self.blog_title[:500]
#поменять текст и тайтл, переименовать евент

	def __str__(self):
		return self.event_text