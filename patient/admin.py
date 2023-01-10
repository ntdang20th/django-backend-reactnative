from django.contrib import admin
from .models import *
from doctor.models import Doctor


# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'uuid', 'patient', 'crutch', 'description', 'is_active']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        user = request.user
        doctor = Doctor.objects.get(user=user)
        patients = Patient.objects.filter(doctor=doctor)
        return qs.filter(patient__in = patients)

@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'gender', 'birth', 'phone_number', 'share_address']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        user = request.user
        doctor = Doctor.objects.get(user=user)
        patients = Patient.objects.filter(doctor=doctor)

        has_pt_id_list = HasPatientFamiliar.objects.filter(patient__in = patients)

        return qs.filter(id__in = has_pt_id_list)

@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'gender', 'birth', 'phone_number', 'share_address']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        user = request.user
        doctor = Doctor.objects.get(user=user)
        patients = Patient.objects.filter(doctor=doctor)

        return qs.filter(id__in = patients.values_list('patient_info'))

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id', 'doctor', 'patient_info']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        user = request.user
        doctor = Doctor.objects.get(user=user)
        return qs.filter(doctor=doctor)

@admin.register(HasPatientFamiliar)
class HasPatientFamiliarAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient', 'familiar']
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        user = request.user
        doctor = Doctor.objects.get(user=user)
        patients = Patient.objects.filter(doctor=doctor)

        return qs.filter(patient__in = patients)