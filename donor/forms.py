from django import forms

from .models import Donor, BloodRequest


class DonorForm(forms.ModelForm):

    class Meta:

        model = Donor

        fields = '__all__'

        widgets = {

            'blood_group': forms.Select(
                choices=[
                    ('A+', 'A+'),
                    ('A-', 'A-'),
                    ('B+', 'B+'),
                    ('B-', 'B-'),
                    ('O+', 'O+'),
                    ('O-', 'O-'),
                    ('AB+', 'AB+'),
                    ('AB-', 'AB-')
                ]
            ),

            'gender': forms.Select(
                choices=[
                    ('Male', 'Male'),
                    ('Female', 'Female'),
                    ('Other', 'Other')
                ]
            )
        }

    def clean_mobile(self):

        mobile = self.cleaned_data['mobile']

        if not mobile.isdigit():

            raise forms.ValidationError(
                "Mobile number should contain only numbers"
            )

        if len(mobile) != 10:

            raise forms.ValidationError(
                "Mobile number must be 10 digits"
            )

        return mobile


class BloodRequestForm(forms.ModelForm):

    class Meta:

        model = BloodRequest

        fields = '__all__'

        widgets = {

            'blood_group': forms.Select(
                choices=[
                    ('A+', 'A+'),
                    ('A-', 'A-'),
                    ('B+', 'B+'),
                    ('B-', 'B-'),
                    ('O+', 'O+'),
                    ('O-', 'O-'),
                    ('AB+', 'AB+'),
                    ('AB-', 'AB-')
                ]
            )
        }

    def clean_mobile(self):

        mobile = self.cleaned_data['mobile']

        if not mobile.isdigit():

            raise forms.ValidationError(
                "Mobile number should contain only numbers"
            )

        if len(mobile) != 10:

            raise forms.ValidationError(
                "Mobile number must be 10 digits"
            )

        return mobile