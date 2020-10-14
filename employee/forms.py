from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        label = {
            'password': 'password'
        }

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None
        forms.ModelForm.__init__(self, *args, **kwargs)

    # custom validation of email
    # def clean_email(self):
    #     if self.clean_data['email'].endWith('@ajay.com'):
    #         return self.clean_data['email']
    #     else:
    #         raise ValidationError("email is not valid")

    def save(self):
        password = self.cleaned_data.pop('password')
        role = self.cleaned_data.pop('role')
        u = super().save()
        u.groups.set([role])
        u.set_password(password)
        u.save()
        return u
