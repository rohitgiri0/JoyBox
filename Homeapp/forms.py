from django import forms
from .models import ConsoleListing

class ConsoleListingForm(forms.ModelForm):
    class Meta:
        model = ConsoleListing
        fields = ['console_name','description','price','location','available','photo1','photo2']