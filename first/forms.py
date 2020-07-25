from django import forms

class Formname(forms.Form):
    key = forms.CharField(max_length=50)
    key.widget.attrs.update({'id':'key'})
    data = forms.CharField(max_length=50)
    data.widget.attrs.update({'id':'data'})
    image = forms.ImageField()
