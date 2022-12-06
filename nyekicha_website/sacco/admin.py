from django.contrib import admin
from .models import *

#admin.site.register(Schedule)
admin.site.register(Sacco_Official)
#admin.site.register(Sacco_Member)
admin.site.register(Vehicle)
admin.site.register(Tag)
admin.site.register(Loan)
admin.site.register(Complaint)
admin.site.register(Transaction)

@admin.register(Sacco_Member)
class Sacco_MemberAdmin(admin.ModelAdmin):
	list_display = ('driver_first_name', 'driver_second_name', 'phone', 'vehicle_num_plate')
	ordering = ('driver_first_name',)
	search_fields = ('driver_first_name', 'vehicle_num_plate')


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
	fields = (('Schedule_date', 'destination'), 'manager', 'driver_name', 'vehicle_num_plate')
	list_display = ('Schedule_date','destination', 'manager', 'driver_name', 'vehicle_num_plate')
	list_filter = ('Schedule_date', 'destination')
	ordering = ('Schedule_date',)