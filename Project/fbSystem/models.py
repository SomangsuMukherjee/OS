from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    review = models.TextField()
    image = models.ImageField(upload_to='feedback_images/', null=True, blank=True)

    def __str__(self):
        return self.name
