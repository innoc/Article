from django.db import models

# Create your models here.
class Article(models.Model):

  CATEGORY_CHOICES = (
    ('fk', 'Facebook'),
    ('go', 'Google'),
    ('apl', 'Apple'),
    ('micro', 'Microsoft'),
  )

  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  publication_date = models.DateTimeField()
  category = models.CharField(max_length=5, choices=CATEGORY_CHOICES,default="fk")
  hero_image = models.ImageField(upload_to='.')
  additional_image = models.ImageField(upload_to='.')
  body_text = models.TextField()

  def __str__(self):             
    return self.title