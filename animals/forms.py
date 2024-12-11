from django import forms
from .models import Animal
from PIL import Image


SPECIES_CHOICE = [
    ('Dog', 'Dog'),
    ('Cat', 'Cat'),
    ('Rodent', 'Rodent'),
    ('Bird', 'Bird'),
    ('Other', 'Other'),
]


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            'name',
            'age',
            'species',
            'description',
            'image',
            'location',
            'is_approachable',
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
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            )
        )
    is_approachable = forms.BooleanField(
        label='Is this animal approachable?',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input'
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.capitalize()

    def clean_owner_duplicate(self):
        name = self.cleaned_data['name']
        owner = self.instance.owner
        if Animal.objects.filter(name=name, owner=owner).exists():
            raise forms.ValidationError(f'You have already registered {name}.')
        return name.capitalize()

    def clean_location(self):
        location = self.cleaned_data['location']
        if len(location) < 3:
            raise forms.ValidationError('The location must be at least 3 characters long.')
        return location.capitalize()

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 0 or age > 100:
            raise forms.ValidationError("Age must be between 0 and 100.")
        return age
