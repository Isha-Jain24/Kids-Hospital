from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,User
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)
 

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin) 