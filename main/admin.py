from django.contrib import admin
from .models import Meeting_Session_FeedBack_Link, Meeting_Session_Files, Reg_Student, Reg_Student_Attendance, Reg_Student_Items, Meeting_Session

# Register your models here.

@admin.register(Reg_Student)
class Reg_Student(admin.ModelAdmin):
    list_display = ['id', 'ieee_id', 'name', 'email', 'university']

@admin.register(Reg_Student_Items)
class Reg_Student_Items(admin.ModelAdmin):
    list_display = ['id', 'student', 't_shirt', 'goodies', 'certificate']

@admin.register(Meeting_Session)
class Meeting_Session(admin.ModelAdmin):
    list_display = ['id', 'speaker_name']

@admin.register(Reg_Student_Attendance)
class Reg_Student_Attendance(admin.ModelAdmin):
    list_display = ['id', 'student', 'session', 'attendance']

@admin.register(Meeting_Session_FeedBack_Link)
class Meeting_Session_FeedBack_Link(admin.ModelAdmin):
    list_display = ['id', 'session', 'graphic_link']

@admin.register(Meeting_Session_Files)
class Meeting_Session_Files(admin.ModelAdmin):
    list_display = ['id', 'title', 'file']
