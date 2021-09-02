from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)


# Create your models here.

class Student(models.Model):
    GENDERS = (
        ("f", "female"),
        ("m", "male"),
        ("u", "Undisclosed")
    )

    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, null=True)
    percentage = models.FloatField()
    age = models.IntegerField(
        null=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(5)
        ]
    )

    institute = models.ForeignKey("Institute", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Institute(models.Model):
    TYPES = (
        ("h", "High School"),
        ("c", "College")
    )

    name = models.CharField(max_length=200)
    type_of_institute = models.CharField(max_length=1, choices=TYPES, null=True)

    def __str__(self):
        return self.name
