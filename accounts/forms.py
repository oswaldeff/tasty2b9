from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="이메일",
        widget=forms.TextInput(attrs={
            "placeholder": "이메일 주소를 입력해주세요",
            "class": "input-group-text"
        })
    )
    password1 = forms.CharField(
        required=True,
        min_length=8,
        max_length=16,
        label="비밀번호",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호(영문 8~16자)",
            "class": "input-group-text"
        })
    )
    password2 = forms.CharField(
        required=True,
        min_length=8,
        max_length=16,
        label="",
        widget=forms.PasswordInput(attrs={
            "placeholder": "비밀번호를 재입력해주세요",
            "class": "input-group-text"
        })
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 존재하는 이메일입니다")
        return email