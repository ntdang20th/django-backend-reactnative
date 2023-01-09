from django.db import models

#---------------------------------user - patient - doctor - device----------------------------
class Province(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True, related_name='district')

    def __str__(self):
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True, related_name='ward')

    def __str__(self):
        return self.name

class ShareAddress(models.Model):
    address = models.CharField(max_length=128, blank=True, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.address + ", " + self.ward.__str__() + ", " + self.district.__str__() + ", " + self.province.__str__()
