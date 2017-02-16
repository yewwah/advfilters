from django import forms

class DocumentForm(forms.Form):
   name = forms.CharField(max_length = 100, required= True)
   document = forms.FileField(required = True)
   
