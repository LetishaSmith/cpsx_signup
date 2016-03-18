from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','email')

class ContactForm(forms.Form):
    # the fields we want in the form
    subject = forms.CharField(max_length=100)
    contact_name = forms.CharField(required=True) # contact's name
    contact_email = forms.EmailField(required=True) # contact's email
    message = forms.CharField(required=True,widget=forms.Textarea) # message to invite friend
    cc_myself = forms.BooleanField(required=False)

