from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Complaint

class MemberRegistrationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']

class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone']

class AdminUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone', 'status', 'commitee_member']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.member = kwargs.pop('member', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        complaint = super().save(commit=False)
        complaint.member = self.member
        if commit:
            complaint.save()
        return complaint
