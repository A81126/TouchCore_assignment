from django.db import models

# Create your models here.
class video(models.Model):
	video=models.FileField(upload_to="video/%y")
	subtitle=models.CharField(max_length=100)


	def __str__(self):
		return self.subtitle
