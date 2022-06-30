from django import forms
from api.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'phone', 'address', 'profession', 'age', 'sex']