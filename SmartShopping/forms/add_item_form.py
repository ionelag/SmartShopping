from django import forms

class AddItemForm(forms.Form):
  denumire = forms.CharField(label="Denumire Item", max_length=256)
  firma_producatoare = forms.CharField(label="Firma Producatoare", max_length=100)
  descriere = forms.CharField(widget=forms.Textarea(attrs={"rows":"2"}))
  greutate = forms.CharField(label="Greutate", max_length=256)
  pret = forms.CharField(label="Pret", max_length=256)
  imagine = forms.FileField()