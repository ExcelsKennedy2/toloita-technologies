from django.db import models

# Create your models here.
class Service(models.Model):
    image = models.ImageField(upload_to="services/", null=True, blank=True)
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=120)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.question

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.IntegerField()
    project = models.CharField(max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.name