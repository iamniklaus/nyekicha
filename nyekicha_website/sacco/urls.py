from django.urls import path, include
from . import views


urlpatterns = [

    path('<int:year>/<str:month>/', views.home, name="home"),
    path('', views.home, name="home"),
    path('schedules', views.all_schedules, name="list-schedules"),
    path('add_schedule', views.add_schedule, name='add-schedule'),
    path('search_schedules', views.search_schedule, name='search-schedule'),
    path('update_schedules/<sch_id>', views.update_schedules, name='update-schedules'),
    path('add_member', views.add_member, name='add-member'),
    path('file_complaint', views.file_complaint, name='file-complaint'),
    path('delete_schedule/<sch_id>', views.delete_schedule, name='delete-schedule'),
    
    path('daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),
]
