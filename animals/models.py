from django.db import models
from main.models import CustomUser
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator


SPECIES_CHOICE = [
    ('dog', 'Dog'),
    ('cat', 'Cat'),
    ('rodent', 'Rodent'),
    ('bird', 'Bird'),
    ('other', 'Other'),
]


class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    species = models.CharField(
        max_length=20,
        choices=SPECIES_CHOICE,
    )
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    is_found = models.BooleanField(default=False)

    def __str__(self):
        return self.name
