from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Session(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    about = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gym_session")
    capacity = models.IntegerField(default=0)
    attendance = models.ManyToManyField(
        User, related_name='session_attendance', blank=True)
    location = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_attending(self):
        return self.attendance.count()
