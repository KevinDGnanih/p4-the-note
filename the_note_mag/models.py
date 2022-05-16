""" Model for The Note Magazine home page """
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """ Class for the post """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mag_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='mag_likes', blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        """ Adding methods for a better readability and user experience """
        ordering = ['-created_on']

    def __str__(self):
        """ The string method to make it easier to read """
        return self.title

    def number_of_likes(self):
        """ Returns the total number of likes on a post """
        return self.likes.count()

    def get_cat_list(self):
        key = self.category
        breadcrumb = ['dummy']
        key = key.parent
        while key is not None:
            breadcrumb.append(key.slug)
            key = key.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
            return breadcrumb[-1:0:-1]


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


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        """ Enforcing that there can't be two categories under
        a parent with same slug """
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'categories'

    def __str__(self):
        full_path = [self.name]
        key = self.parent
        while key is not None:
            full_path.append(key.name)
            key = key.parent
        return ' -> '.join(full_path[::-1])
