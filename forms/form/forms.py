from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=33)
    type1 = forms.CharField(max_length=33)

