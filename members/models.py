from datetime import datetime
from uuid import uuid4

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Date(models.Model):
    date = models.DateField(auto_now=True, unique=True)

    def __str__(self):
        return str(self.date)


class Member(models.Model):
    class Genders(models.TextChoices):
        MALE = "m", _("Male")
        FEMALE = "f", _("Female")

    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=8)
    email = models.EmailField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=Genders.choices)
    specializations = models.ManyToManyField(
        Specialization, related_name='member')
    activities = models.ManyToManyField(
        Date, related_name="activity", blank=True)
    last_activity = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to="members", blank=True, null=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.fullname}"

    def save(self, *args, **kwargs) -> None:
        if self.id is None:
            self.slug = slugify(str(uuid4()))

        return super().save(*args, **kwargs)

    def is_activity_updated(self):
        today = Date.objects.get(date=datetime.today())
        # Checks if there is today's date
        if not self.activities.contains(today):
            self.activities.add(today)
            self.last_activity = datetime.now()
            self.save()
            return True
        return False
