from django.db import models
from django.core.validators import MinlengthValidator


class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        help_text="Enter a nickname for your car (eg. Mcqueen)",
        validators=[MinlengthValidator(2, "Nickname must be longer than 1 character")],
    )
    make = models.ForeignKey("Make", on_delete=models.CASCADE, null=False)
    mileage = models.PositiveIntegerField()
    comments = models.Charfield(max_length=300)

    def __str__(self):
        return self.nickname


class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a make (eg. Dodge)",
        validators=[MinlengthValidator(2, "Make must be greater thn 1 character")],
    )

    def __str__(self):
        """String to represent the make obbject"""
        return self.name
