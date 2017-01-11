from django import forms

class DocumentForm(forms.Form):
   name = forms.CharField(max_length = 100)
   document = forms.FileField()
   
