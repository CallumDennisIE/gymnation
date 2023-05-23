from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Session(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    about = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    trainer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gym_session")
    capacity = models.PositiveSmallIntegerField(default=0)
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
    modified_on = models.DateTimeField(auto_now=True)
    # rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Membership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member_type = models.CharField(max_length=200, default="Basic")
    start_date = models.DateField(auto_now_add=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    # https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Membership.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.membership.save()
