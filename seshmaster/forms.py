from django import forms 
from seshmaster.models import User,Image,Nightclub,Review

class nightclub_form(forms.ModelForm):

         
    class Meta:
        model = Nightclub
        fields = ("name","music_genre","price","description","location","image") 
        

class signup_form(forms.ModelForm):

    class Meta:
        model = User
        fields = ("name","email","password","picture") 
