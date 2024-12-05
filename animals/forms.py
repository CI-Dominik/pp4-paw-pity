from django import forms
from .models import Animal
from PIL import Image


SPECIES_CHOICE = [
    ('dog', 'Dog'),
    ('cat', 'Cat'),
    ('rodent', 'Rodent'),
    ('bird', 'Bird'),
    ('other', 'Other'),
]


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'name',
            'age',
            'species',
            'description',
            'image'
        ]

    name = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            )
        )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control', 'min': 0, 'max': 100
                }
            ),
        initial=0
    )
    species = forms.ChoiceField(
        choices=SPECIES_CHOICE,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 'rows': 3
                }
            ), required=False
        )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})

    )

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.capitalize()

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0 or age > 100:
            raise forms.ValidationError("Age must be between 0 and 100.")
        return age

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        width, height = img.size
        if width > 1548 or height > 1548:
            raise forms.ValidationError('The image is too big. Please choose a picture with less than 1548 pixels in height or width.')
        return image
