from django import forms 
from seshmaster.models import UserProfile,Image,Nightclub
from django.contrib.auth.models import User 

class nightclub_form(forms.ModelForm):

         
    class Meta:
        model = Nightclub
        fields = ("name","music_genre","price","description","location","img") 
        

class signup_form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ("username","email","password")

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)

