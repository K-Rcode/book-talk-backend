from django.db import models


# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.CharField(max_length=100)
   image = models.URLField()
   category = models.CharField(max_length=100)
   description = models.TextField()
   book_owner = models.ForeignKey('users.User', related_name='books', on_delete=models.CASCADE)

   def __str__(self):
       return self.title



class Comment(models.Model):
    # look at time stamp later
    time_stamp = models.DateField(auto_now=True)
    owner = models.ForeignKey('users.User', related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
