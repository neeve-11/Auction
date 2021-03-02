from django.forms import ModelForm
from poll.models import user,bidding,wishlist,comment
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
#
class register_form(ModelForm):
     email = forms.EmailField(validators=[validators.validate_email],required=True, error_messages={'required' : 'Please enter Email id', 'validators' : 'Enter a valid email id'})
     password = forms.CharField(required=True, widget=forms.PasswordInput)
     c_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)
     class Meta:
         model = user
         fields = ['username','email','first_name','last_name','password']
     def clean(self):
          cleaned_data = super().clean()
          pword = cleaned_data.get('password')
          c_pword = cleaned_data.get('c_password')
          if not pword == c_pword:
              raise forms.ValidationError('Confirmation password is not same as password')

class login_form(ModelForm):
    email = forms.EmailField(validators=[validators.validate_email], required=True, error_messages={'required' : 'Please enter Email id', 'validators' : 'Enter a valid email id'})
    password = forms.CharField(required=True, widget=forms.PasswordInput, error_messages={'required' : 'Please enter password'})
    class Meta:
        model = user
        fields = ['email', 'password']

class makebid_form(ModelForm):
    name = forms.CharField(required=True)
    price = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = bidding
        fields = '__all__'
        exclude = ['user']
# class comment_form(ModelForm):
#     c_comment = forms.CharField(widget=forms.Textarea)
#     pdt = forms.CharField(widget)
#     class Meta:
#         model = comment
#         fields = '__all__'
#         exclude = ['user', 'item']

class bid_form(ModelForm):
     price = forms.CharField(required=True)
     class Meta:
         model = bidding
         fields =['price']
