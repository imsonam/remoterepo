from django import forms


class EmpForm(forms.Form):
    name = forms.CharField(
        label="enter your name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your name'
            }

        )
    )
    sal = forms.IntegerField(
        label="enter your sal",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your salary'
            }

        )
    )
    mobile = forms.IntegerField(
        label="enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile number'
            }

        )
    )
    email = forms.EmailField(
        label="enter your email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }

        )
    )
    location = forms.CharField(
        label="enter your location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your location'
            }

        )
    )
