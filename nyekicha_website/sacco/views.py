from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Schedule
from .forms import ScheduleForm, MemberForm, FileComplaintForm

from django_daraja.mpesa.core import MpesaClient


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
	name = "Nyekicha Sacco"
	month = month.capitalize()
	# convert month from name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	#create calendar
	cal = HTMLCalendar().formatmonth(
		year,
		month_number)

	#get current year
	now = datetime.now()
	current_year = now.year

	#get current time
	time = now.strftime('%I:%M %p')

	return render(request, 
		'sacco/home.html', {
		'name':name,
		'year': year,
		'month': month,
		'month_number': month_number,
		'cal': cal,
		'current_year': current_year,
		'time': time,
		})

def all_schedules(request):
	schedule_list = Schedule.objects.all().order_by('-Schedule_date')

	return render(request, 'sacco/Schedules_list.html', {'schedule_list':schedule_list})

def add_schedule(request):
	submitted = False
	if request.method == "POST":
		form = ScheduleForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_schedule?submitted=True')
	else:
		form = ScheduleForm
		if 'submitted' in request.GET:
			submitted = True


	context = {'form':form, 'submitted':submitted}

	return render(request, 'sacco/add_schedule.html', context)

def search_schedule(request):
	if request.method == "POST":
		searched = request.POST['searched']
		schedules = Schedule.objects.filter(destination__contains=searched)

		return render(request, 'sacco/search_schedules.html', {'searched':searched, 'schedules':schedules})

	else:
		return render(request, 'sacco/search_schedules.html', {})


def update_schedules(request, sch_id):
	schedule = Schedule.objects.get(pk=sch_id)
	form = ScheduleForm(request.POST or None, instance=schedule)
	if form.is_valid():
		form.save()
		return redirect('list-schedules')
		
	return render(request, 'sacco/update_schedules.html', {'schedule':schedule, 'form':form})

def add_member(request):
	submitted = False
	if request.method == "POST":
		form = MemberForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_member?submitted=True')
	else:
		form = MemberForm
		if 'submitted' in request.GET:
			submitted = True


	context = {'form':form, 'submitted':submitted}

	return render(request, 'sacco/add_member.html', context)

def file_complaint(request):
	submitted = False
	if request.method == "POST":
		form = FileComplaintForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/file_complaint?submitted=True')
	else:
		form = FileComplaintForm
		if 'submitted' in request.GET:
			submitted = True


	context = {'form':form, 'submitted':submitted}

	return render(request, 'sacco/file_complaint.html', context)

def delete_schedule(request, sch_id):
	schedule = Schedule.objects.get(pk=sch_id)
	schedule.delete()
	return redirect('list-schedules')


def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '0791835026'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body