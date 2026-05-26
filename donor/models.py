from django.core.validators import RegexValidator
from django.db import models


class Donor(models.Model):

    name = models.CharField(
        max_length=100
    )

    age = models.IntegerField()

    gender = models.CharField(
        max_length=10
    )

    blood_group = models.CharField(
        max_length=5
    )

    city = models.CharField(
        max_length=100
    )

    mobile = models.CharField(

    max_length=10,

    validators=[

        RegexValidator(

            regex=r'^[0-9]{10}$',

            message='Enter valid 10 digit mobile number'

        )

    ]

)
    email = models.EmailField()

    address = models.TextField()

    available = models.BooleanField(
        default=True
    )
    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):

        return self.name


class BloodRequest(models.Model):

    patient_name = models.CharField(
        max_length=100
    )

    blood_group = models.CharField(
        max_length=5
    )

    city = models.CharField(
        max_length=100
    )

    mobile = models.CharField(
        max_length=15
    )

    units = models.IntegerField(
        default=1
    )
    status = models.CharField(
        max_length=20,
        default='Pending'
     )
    def __str__(self):

        return self.patient_name