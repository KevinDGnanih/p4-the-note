""" Model for The Note Magazine home page """
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from mptt.models import MPTTModel, TreeForeignKey
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
CATEGORY = [('Music', 'Music'), ('Live', 'Live'), ('Review', 'Review'), ('Playlist', 'Playlist') ]


class Post(models.Model):
    """ Class for the post """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY, default='Music')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mag_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='mag_likes', blank=True)

    class Meta:
        """ Adding methods for a better readability and user experience """
        ordering = ['-created_on']



    def __str__(self):
        """ The string method to make it easier to read """
        return self.title

    def number_of_likes(self):
        """ Returns the total number of likes on a post """
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')

    def get_success_url(self):
        return reverse_lazy('home')

    

class Category(models.Model):
    name = models.CharField(max_length=50, choices=CATEGORY, default='Music')
    
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')



class Comment(models.Model):
    """ Class for the comment """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ Adding helpers for a better readability and user experience"""
        ordering = ['created_on']

    def __str__(self):
        """ Display the comment and the author """
        return f"Comment {self.body} by {self.name}"