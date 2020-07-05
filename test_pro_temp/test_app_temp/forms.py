from django import forms
from test_app_temp.models import PUser,UserInfo
from django.contrib.auth.models import User

class Aform(forms.ModelForm):
    class Meta:
        model = PUser
        fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username","password","email"]

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ["portfolio","dp"]
