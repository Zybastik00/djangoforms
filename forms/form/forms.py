from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=13)
    number_phone = forms.CharField(max_length=13)

