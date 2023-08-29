from django import forms

from . import models

from .models import User
import re
class AdminSigupForm(forms.ModelForm):

    class Meta:

        model=User

        fields=['first_name','last_name','username','email','password']

        widgets = {

        'password': forms.PasswordInput()

        }
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError('Name should contain only characters')
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError('Name should contain only characters')
        return last_name
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' not in username or not any(char.isdigit() for char in username):
            raise forms.ValidationError('Username must contain "@" and at least one number.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use.')  
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user=User.objects.filter(email=email).first()
        if user and user.groups.filter(name='ADMIN').exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

 

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
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError('Name should contain only characters')
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError('Name should contain only characters')
        return last_name
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' not in username or not any(char.isdigit() for char in username):
            raise forms.ValidationError('Username must contain "@" and at least one number.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use.')  
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user=User.objects.filter(email=email).first()
        if user and user.groups.filter(name='DOCTOR').exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password

class DoctorForm(forms.ModelForm):

    class Meta:

        model=models.Doctor

        fields=['address','mobile','department','status','profile_pic']
    
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        mobile_regex= r'^\d{10}$'
        if not mobile.isdigit(): 
            raise forms.ValidationError('Phone number must contain only digits.')
        elif not re.match(mobile_regex,mobile):
            raise forms.ValidationError('Enter a valid 10 digit phone number.')
        return mobile
 

 

 

#for teacher related form

class PatientUserForm(forms.ModelForm):

    class Meta:

        model=User

        fields=['first_name','last_name','username','email','password']

        widgets = {

        'password': forms.PasswordInput()

        }
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError('Name should contain only characters')
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError('Name should contain only characters')
        return last_name
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if '@' not in username or not any(char.isdigit() for char in username):
            raise forms.ValidationError('Username must contain "@" and at least one number.')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use.')  
        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user=User.objects.filter(email=email).first()
        if user and user.groups.filter(name='PATIENT').exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters long.')
        return password
   
class PatientForm(forms.ModelForm):

    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")

    class Meta:

        model=models.Patient

        fields=['address','mobile','status','symptoms','profile_pic']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        mobile_regex= r'^\d{10}$'
        if not mobile.isdigit(): 
            raise forms.ValidationError('Phone number must contain only digits.')
        elif not re.match(mobile_regex,mobile):
            raise forms.ValidationError('Enter a valid 10 digit phone number.')
        return mobile

 

 

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