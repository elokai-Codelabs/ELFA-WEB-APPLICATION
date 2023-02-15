from django.db import models

# Create your models here.
class SMS(models.Model):
    sender_id = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    messages_sent = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    