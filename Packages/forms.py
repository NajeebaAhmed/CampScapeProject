from django import forms
from .models import PackageDetails

class PackageForm(forms.ModelForm):
    class Meta:
        model = PackageDetails
        fields = '__all__'
        