from django import forms
from lms_app.models import UserType
from lms_app.models import User

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = "__all__"

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)