from django.db import models

class Submission(models.Model):
    message = models.CharField(max_length=600, default="no message")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} shared a message : {self.message}"
