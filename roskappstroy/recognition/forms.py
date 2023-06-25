from django import forms
from django.core.exceptions import ValidationError


class TextForm(forms.Form):
    text_for_recognition = forms.CharField(max_length=300)


class FileForm(forms.Form):
    data_csv = forms.FileField(required=False)

    # def clean(self):
    #     cd = self.cleaned_data

    #     password1 = cd.get("data_csv")

    #     if password1 != password2:
    #         #Or you might want to tie this validation to the password1 field
    #         raise ValidationError("Passwords did not match")


    #     return cd