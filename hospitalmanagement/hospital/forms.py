from django import forms

from . import models

from .models import User

 

class AdminSigupForm(forms.ModelForm):

    class Meta:

        model=User

        fields=['first_name','last_name','username','email','password']

        widgets = {

        'password': forms.PasswordInput()

        }

 

class SendOTPForm(forms.Form):

    class Meta:

 

        model = User

        fields = ('email')

 

class DoctorUserForm(forms.ModelForm):

    class Meta:

        model=User

        fields=['first_name','last_name','username','email','password']

        widgets = {

        'password': forms.PasswordInput()

        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user=User.objects.filter(email=email).first()
        if user and user.groups.filter(name='DOCTOR').exists():
            raise forms.ValidationError("This email is already registered.")
        return email

class DoctorForm(forms.ModelForm):

    class Meta:

        model=models.Doctor

        fields=['address','mobile','department','status','profile_pic']

 

 

 

#for teacher related form

class PatientUserForm(forms.ModelForm):

    class Meta:

        model=User

        fields=['first_name','last_name','username','email','password']

        widgets = {

        'password': forms.PasswordInput()

        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user=User.objects.filter(email=email).first()
        if user and user.groups.filter(name='PATIENT').exists():
            raise forms.ValidationError("This email is already registered.")
        return email

class PatientForm(forms.ModelForm):

   

    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")

    class Meta:

        model=models.Patient

        fields=['address','mobile','status','symptoms','profile_pic']

 

 

 

class AppointmentForm(forms.ModelForm):

    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")

    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")

    class Meta:

        model=models.Appointment

        fields=['description','status']

 

 

class PatientAppointmentForm(forms.ModelForm):

    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")

    class Meta:

        model=models.Appointment

        fields=['description','status']

 

 

#for contact us page

class ContactusForm(forms.Form):

    Name = forms.CharField(max_length=30)

    Email = forms.EmailField()

    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))