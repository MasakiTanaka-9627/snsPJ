from django import forms
from django.core.exceptions import ValidationError
 
 
class UserForm(forms.Form):
    name = forms.CharField(label='ユーザー名', required=True, max_length=100)
    email = forms.EmailField(label='メールアドレス', required=True, max_length=100, widget=forms.EmailInput)
    password = forms.CharField(label='パスワード', required=True ,widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("名前を入力して下さい")
        return cleaned_data