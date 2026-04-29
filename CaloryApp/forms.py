from django import forms
from .models import *


class UpdatedProfileForm(forms.ModelForm):
    class Meta:
        model = UpdatedProfileModel
        fields = '__all__'
        exclude = ['user', 'bmr']




class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItemModel
        fields = ['item_name', 'calory']