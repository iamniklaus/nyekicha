from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

import uuid

# Create your models here.

class Schedule(models.Model):
	Schedule_date = models.DateTimeField('Schedule Date')
	destination = models.CharField('Destination',max_length=200)
	manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	driver_name = models.CharField('Driver Name',max_length=60)
	vehicle_num_plate = models.CharField('Number Plate',max_length=60)

	def __str__(self):
		return self.destination


class Sacco_Official(models.Model):
    first_name = models.CharField('First Name',max_length=200, null=True)
    second_name = models.CharField('Second Name',max_length=200, null=True)
    phone = models.CharField('Contact Phone',max_length=200, null=True)
    email = models.EmailField('Email',max_length=200, null=True)
    Department = models.CharField('Department Name',max_length=200, null=True)
    Position = models.CharField('Office Position',max_length=200, null=True)
    
    def __str__(self):
        return self.first_name + '' + self.second_name

class Sacco_Member(models.Model):
    driver_first_name = models.CharField('First Name',max_length=200, null=True)
    driver_second_name = models.CharField('Second Name',max_length=200, null=True)
    phone = models.CharField('Contact Phone',max_length=200, null=True)
    email = models.EmailField('Email',max_length=200, null=True, blank=True)
    vehicle_num_plate = models.CharField('Number Plate',max_length=200, null=True)

    def __str__(self):
        return self.driver_first_name + '' + self.driver_second_name

class Vehicle(models.Model):
    vehicle_num_plate = models.CharField('Number Plate',max_length=200, null=True)
    driver = models.ForeignKey(Sacco_Member, null=True, on_delete=models.SET_NULL)
    brand = models.CharField('Car Brand',max_length=200, null=True)
    Insurance_comp = models.CharField('Insurance Company',max_length=200, null=True)
    service_comp = models.CharField('Service Company',max_length=200, null=True)

    def __str__(self):
        return self.vehicle_num_plate

class Tag(models.Model):
    name = models.CharField('Name',max_length=200, null=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    STATUS = (
        ('Performing', 'Performing'),
        ('Late', 'Late'),
        ('Overdue', 'Overdue'),
        ('Default', 'Default'),
        ('Paid', 'Paid'),
    )

    driver = models.ForeignKey(Sacco_Member, null=True, on_delete=models.SET_NULL)
    loan_id = models.AutoField(primary_key=True)
    loan_amount = models.CharField('Loan_Amount',max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    interest_rate = models.CharField('Rate Of Interest',max_length=200, null=True)
    status = models.CharField('Status Of Loan',max_length=200, null=True, choices=STATUS)
    Tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.driver.driver

class Complaint(models.Model):
    name = models.CharField('Your Name', max_length=200, null=True)
    vehicle_num_plate = models.CharField('Vehicle No. Plate', max_length=200, null=True)
    subject = models.CharField('Subject', max_length=400, null=True)
    message = models.CharField('Your Complaint', max_length=1000, null=True)



STATUS = ((1, "Pending"), (0, "Complete"))

class Transaction(models.Model):
    """This model records all the mpesa payment transactions"""
    transaction_no = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    checkout_request_id = models.CharField(max_length=200)
    reference = models.CharField(max_length=40, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.CharField(max_length=10)
    status = models.CharField(max_length=15, choices=STATUS, default=1)
    receipt_no = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return f"{self.transaction_no}"