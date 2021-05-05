from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
	title = models.CharField(max_length=255, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)	
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	publish_date = models.DateTimeField()

	def __str__(self):
		return self.title 
		


class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now
	) 
	publish_date = models.DateTimeField(
		blank=True, null=True
	)


	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
