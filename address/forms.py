from django import forms
from address.models import ShareAddress


class CustomAddressForm(forms.ModelForm):
    class Meta:
        model = ShareAddress
        fields = [
            'address',
            'ward',
        ]
        widgets = {
            'address': forms.TextInput(),
        }