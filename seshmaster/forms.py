from django import forms 
from seshmaster.models import User,Image,Nightclub,Review

class nightclub_form(forms.ModelForm):

         name = forms.CharField(max_length=128,help_text="Please enter the location name.")
         music_genre = forms.CharField(max_length=100,help_text="What is the music like here?")
         price = forms.CharField(max_length=128,help_text="Price range?")
         description = forms.CharField(max_length=400,help_text="Little inside on what the place is like ;)")
         location = forms.CharField(max_length=128,help_text="Where can people find this?")
         score= forms.CharField(max_length=128,help_text="leave a score")

         class Meta:
                  model = Nightclub
                  fields = ("name",) 
