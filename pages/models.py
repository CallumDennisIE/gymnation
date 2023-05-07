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
    location = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_attending(self):
        return self.attendance.count()


class Review(models.Model):
    LOWEST = 1
    LOW = 2
    NORMAL = 3
    HIGH = 4
    HIGHEST = 5
    RATING_CHOICES = (
        (LOWEST, '1'),
        (LOW, '2'),
        (NORMAL, '3'),
        (HIGH, '4'),
        (HIGH, '5'),
    )

    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
