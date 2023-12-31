from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import *
from quiz.models import *

#to register
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text='Required. Add a valid email adress')

	class Meta:
		model = Account 
		fields = ("email", "username", "password1", "password2", "is_admin")

class setGrade(forms.ModelForm):
	student=forms.ModelChoiceField(queryset=Account.objects.all())
	subject=forms.ModelChoiceField(queryset=Subject.objects.all())
	letter_grade=forms.ModelChoiceField(queryset=LetterGrades.objects.all())
	percent=forms.DecimalField(max_digits=5)

	class Meta:
		model = Grade
		fields = ("student","letter_grade","subject","percent") 

class setWeight(forms.ModelForm):
	crit = forms.CharField()
	weight = forms.IntegerField(max_value=100)
 	
	class Meta:
		model = Weights
		fields = ('crit','weight')


#to authenticate
class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid Login")

#updates the values changed
class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account 
		fields = ('email', 'username')

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email 
			raise forms.ValidationError('Email "%s" is already iin use.' % email)

	#this method will let us get cleaned data from the given
	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username 
			raise forms.ValidationError('Username "%s" is already in use.' % username)








