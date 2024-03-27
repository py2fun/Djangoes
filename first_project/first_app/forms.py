from django import forms

class TestForm(forms.Form):
    text = forms.CharField(min_length=7) 
    boolean = forms.BooleanField()
    integer = forms.IntegerField()
    email = forms.EmailField()