from django import forms

from .models import SignUp

class ContactForm(forms.Form):
	email = forms.EmailField()
	message = forms.CharField()


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['email']
		### exclude = ['full_name']
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		# if not domain == 'USC':
		# 	raise forms.ValidationError("Please make sure you use your USC email.")
		if not extension == ".com":
			raise forms.ValidationError("Please use a valid .com email address")
		return email

	# def clean_full_name(self):
	# 	full_name = self.cleaned_data.get('full_name')
	# 	#write validation code.
	# 	return full_name