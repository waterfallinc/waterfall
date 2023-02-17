from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            try:
                self.instance = self.instance.user.profile
            except Profile.DoesNotExist:
                self.instance = Profile(user=self.instance.user)
        # fields = ['image', 'bio']