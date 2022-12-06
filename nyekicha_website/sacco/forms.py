from django import forms
from django.forms import ModelForm
from .models import Schedule, Sacco_Member, Complaint

#create a schedule form
class ScheduleForm(ModelForm):
	class Meta:
		model = Schedule
		fields = ('Schedule_date', 'destination', 'manager', 'driver_name', 'vehicle_num_plate')
		labels = {
			'Schedule_date': 'YYYY-MM-DD HH:MM:SS',
			'destination': '',
			'manager': 'Manager',
			'driver_name': '',
			'vehicle_num_plate': '',
		}
		widgets =  {
			'Schedule_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Date And Time'}),
			'destination': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter The Destination'}),
			'manager': forms.Select(attrs={'class':'form-select', 'placeholder': 'Select Active Manager'}),
			'driver_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name Of Driver'}),
			'vehicle_num_plate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Vehicle Number Plate'}),
		}


class MemberForm(ModelForm):
	class Meta:
		model = Sacco_Member
		fields = ('driver_first_name', 'driver_second_name', 'phone', 'email', 'vehicle_num_plate')
		labels = {
			'driver_first_name': '',
			'driver_second_name': '',
			'phone': '',
			'email': '',
			'vehicle_num_plate': '',
		}
		widgets =  {
			'driver_first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'driver_second_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Second Name'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}),
			'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'vehicle_num_plate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vehicle No. Plate'}),
		}


class FileComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		fields = ('name', 'vehicle_num_plate', 'subject', 'message')
		labels = {
			'name': '',
			'vehicle_num_plate': '',
			'subject': '',
			'message': '',
		}
		widgets =  {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Full Names'}),
			'vehicle_num_plate': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vehicle No. Plate'}),
			'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Subject'}),
			'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Complaint'}),
		}