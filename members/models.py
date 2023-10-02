from uuid import uuid4

from django.db import models
from django.utils.text import slugify


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
        MALE = "m", "Male"
        FEMALE = "f", "Female"

    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=8)
    email = models.EmailField()
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=Genders.choices)
    specializations = models.ManyToManyField(Specialization, related_name='member')
    dates = models.ManyToManyField(Date, related_name="activity", blank=True)
    image = models.ImageField(upload_to="members", blank=True, null=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.id}. {self.fullname}"

    def save(self, *args, **kwargs) -> None:
        if self.id is None:
            self.slug = slugify(str(uuid4()))

        super().save(*args, **kwargs)
