from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class Registerforms(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'username' , 'class':'custom_input'}))
	password = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'password' , 'type':'password', 'class':'custom_input'}))
	re_password = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'re_password' , 'type':'password', 'class':'custom_input'}))

	def clean_re_password(self):
		password = self.cleaned_data.get('password')
		re_password = self.cleaned_data.get('re_password')
		if len(password) < 8:
			raise forms.ValidationError('Password is too short ↨')
		if password != re_password:
			raise forms.ValidationError('password and re_password Not matched . Focus!')
		return re_password

	def clean_username(self):
		user = self.cleaned_data.get('username')
		if len(user)<5:
			raise forms.ValidationError('Username is too short ↨')
		if User.objects.filter(username = user).exists():
			raise forms.ValidationError('This username already taken ↔')
		return user

class Loginforms(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'username', 'class':'custom_input'}))
	password = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'password' , 'type':'password', 'class':'custom_input'}))
