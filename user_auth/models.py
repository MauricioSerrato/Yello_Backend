from django.db import models
from django.contrib.auth.models import User



# Create your models here.

# we are creating model here for posts 
# 
# using on delete & cascade - this allows the post to be deleted IF the user itself has been deleted
#
#

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=2000)
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description


