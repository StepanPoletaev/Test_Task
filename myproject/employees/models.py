from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)
    leader = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    transfer_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'id: {self.pk} | {self.full_name}'


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    leader = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='departments')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.pk} | {self.name}'


