from django.db import models

# Create your models here.

class Beat(models.Model):
	beat = models.FileField(upload_to='beats', null=True, blank=True)
	image = models.ImageField(upload_to='beat_image', null=True, blank=True)
	title = models.CharField(max_length=100)
	produced_By = models.CharField(max_length=100)

	def __str__(self):
		return self.title


class Instrument(models.Model):
	image = models.ImageField(upload_to='Instrument_images')
	sound = models.FileField(upload_to='Instrument_sounds')
	name = models.CharField(max_length=100)


	def __str__(self):
		return self.name


class Guitar(models.Model):
	image = models.ImageField(upload_to='Guitar_images')
	sound = models.FileField(upload_to='Guitar_sounds')
	name = models.CharField(max_length=100)


	def __str__(self):
		return self.name

class Piano(models.Model):
	image = models.ImageField(upload_to='Piano_images')
	sound = models.FileField(upload_to='Piano_sounds')
	name = models.CharField(max_length=100)


	def __str__(self):
		return self.name


class Marimba(models.Model):
	image = models.ImageField(upload_to='Maromba_images')
	sound = models.FileField(upload_to='Marimba_sounds')
	name = models.CharField(max_length=100)


	def __str__(self):
		return self.name

class Trumpets(models.Model):
	image = models.ImageField(upload_to='Trumpet_images')
	sound = models.FileField(upload_to='Trumpets_sounds')
	name = models.CharField(max_length=100)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Trumpets'




