from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=1024)
    from_email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(required=False, max_length=32)
    message = forms.CharField(label='Сообщение', required=True)