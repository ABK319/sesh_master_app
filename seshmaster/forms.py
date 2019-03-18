from django import forms 
from seshmaster.models import UserProfile,Image,Nightclub,Review, NCImage
from django.contrib.auth.models import User 

class nightclub_form(forms.ModelForm):

         
    class Meta:
        model = Nightclub
        fields = ("name","music_genre","price","description","location","image") 
        

class signup_form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ("username","email","password")

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)
		
class NightclubReviewForm(forms.ModelForm):
		
	class Meta:
		model = Review
		fields = ('nightclub', 'user', 'score', 'Comment')
		
class NightclubUserImage(forms.ModelForm):

	class Meta:
		model = NCImage
		fields = ('image',)
	

