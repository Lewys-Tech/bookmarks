import requests
from django.core.files.base import ContentFile
from django import forms
from django.utils.text import slugify
from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {'url': forms.HiddenInput}

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[-1].lower()  # Corrected to .lower()

        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)

        # Get the file extension and format the image name
        extension = image_url.rsplit('.', 1)[-1].lower()
        image_name = f'{name}.{extension}'

        # Download image from the given URL
        response = requests.get(image_url)
        if response.status_code == 200:
            image.image.save(image_name, ContentFile(response.content), save=False)

            if commit:
                image.save()
        return image