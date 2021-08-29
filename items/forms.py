from django import forms
from .models import Item
 
class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name", "description", "price", "image" )