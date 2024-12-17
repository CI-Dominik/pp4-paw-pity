from django.db import models
from main.models import CustomUser
from django.contrib import admin
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
    name = models.CharField(max_length=20)
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
    description = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    location = models.CharField(max_length=100, blank=False, null=False)
    is_approachable = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'species', 'owner', 'location', 'is_approachable')
