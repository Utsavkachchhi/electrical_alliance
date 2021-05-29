from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Dealers, Distributors, Item, Menu, Feedback


class DealerSignUpForm(forms.ModelForm):
	email = forms.EmailField( required=True, )

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

		def save(self, commit=True):
			user = super().save(commit=False)
			user.is_dealers = True
			if commit:
				user.save()
			return user


class DistributorsSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

		def save(self, commit=True):
			user = super().save(commit=False)
			user.is_distributors = True
			if commit:
				user.save()
			return user


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Dealers
		fields ='__all__'


class DistributorsForm(forms.ModelForm):
	class Meta:
		model = Distributors
		fields = '__all__'


class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields ='__all__'
