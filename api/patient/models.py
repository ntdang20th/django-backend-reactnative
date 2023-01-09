from django.db import models

from address.models import ShareAddress
from backend import settings
from doctor.models import Doctor




class Familiar(models.Model):
    gender_choice = ((0, 'Nữ'), (1, 'Nam'), (2, 'Không rõ'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=gender_choice, default=0)
    birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    share_address = models.ForeignKey(ShareAddress, on_delete=models.CASCADE)


class PatientInfo(models.Model):
    gender_choice = ((0, 'Nữ'), (1, 'Nam'), (2, 'Không rõ'))
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.IntegerField(choices=gender_choice, default=0)
    birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    share_address = models.ForeignKey(ShareAddress, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + " " + self.first_name

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_info = models.ForeignKey(PatientInfo, on_delete=models.CASCADE, related_name='info')


class HasPatientFamiliar(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    familiar = models.ForeignKey(Familiar, on_delete=models.CASCADE)


class Device(models.Model):
    crutch_type = (('1', 'Crutch 1'),
                   ('2', 'Crutch 2'))
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    uuid = models.CharField(max_length=128, default='')
    description = models.TextField(max_length=255, default='')
    crutch = models.CharField(choices=crutch_type, max_length=255, default=0)
    prediction = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

