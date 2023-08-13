from django.db import models

from apps.countries.models import Country


class University(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    class SexChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    sex = models.CharField(max_length=6, choices=SexChoices.choices)
    universities = models.ManyToManyField(University, blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class StudentPass(models.Model):
    number = models.CharField(max_length=10)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
