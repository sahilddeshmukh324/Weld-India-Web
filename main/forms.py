from django import forms
from .models import UploadedFile,Inquiry

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['image']


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'company_name', 'phone', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(InquiryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your company name'})  # ✅ Added company name styling
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your phone number'})  # ✅ Updated phone_number
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your message'})
