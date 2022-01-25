from django import forms
from lms_app.models import UserType

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = "__all__"