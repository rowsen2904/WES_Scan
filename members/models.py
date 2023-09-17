from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class Date(models.Model):
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.date
    


class Member(models.Model):
    class Genders(models.TextChoices):
        MALE = "m", "Male"
        FEMALE = "f", "Female"

    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=8)
    email = models.EmailField() 
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=Genders.choices)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.id}. {self.specialization} | {self.fullname}"
    
