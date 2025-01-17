from django.db import models

class Movies(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	category = models.CharField(max_length=100)
	duration = models.CharField(max_length=10)
	img = models.URLField()
	rating = models.DecimalField(max_digits=4, decimal_places=2)
	year = models.CharField(max_length=10, null=True, blank=True)
	video = models.URLField(null=True, blank=True)

	class Meta:
		verbose_name="Movie"
		verbose_name_plural="Movies"
		ordering=["title"]

	def __str__(self):
		return self.title
