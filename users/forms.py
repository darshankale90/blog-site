from django import forms
from  django.contrib.auth.models import User

from users.models import post
# from  app.models import profiledb


class LoginForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','password')

class PostData(forms.ModelForm):
    class Meta():
        model = post
        fields = ('text',)
