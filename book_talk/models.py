from django.db import models


# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=100)
   author = models.CharField(max_length=100)
   image = models.URLField(blank=True)
   category = models.CharField(max_length=100, blank=True)
   description = models.TextField()
   owner = models.ForeignKey('users.User', related_name='books', on_delete=models.CASCADE)
   publisher = models.CharField(max_length=100, blank=True)
   published_date = models.CharField(max_length=100, blank=True)
   google_id = models.CharField(max_length=100, blank=True)
   preview_link = models.URLField(blank=True)

   def __str__(self):
       return self.title



class Comment(models.Model):
    # look at time stamp later
    time_stamp = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('users.User', related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.body
