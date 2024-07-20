from typing import Any, Dict
from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")
    
class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again.')
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required=False, #so that it is not visible in the form
                                 widget=forms.HiddenInput, #it is a hidden input field so that humans cannot fill it
                                 validators=[validators.MaxLengthValidator(0)]) # this validator is used to check for length and here it is to have 0 characters.
    
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("Bot has given the input")
        return botcatcher

    def clean(self): # this method is used to clean the entire form
        all_clean_data = super().clean() # this is going to return all the clean data from the entire form
        email = all_clean_data['email']
        verified_email = all_clean_data['verify_email']

        if(email != verified_email):
            raise forms.ValidationError("The emails do not match.")
