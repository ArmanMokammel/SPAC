from insb_spac import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

app_name="main"

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/reg_students/', views.reg_students, name='reg_students'),
    path('dashboard/reg_students_attendance/', views.reg_students_attendance, name='reg_students_attendance'),
    path('dashboard/reg_students_attendance/<int:session_id>', views.reg_students_attendance_main, name='reg_students_attendance_main'),
    path('dashboard/import_csv/', views.import_csv, name='import_csv'),
    path('dashboard/reg_student_details/<str:reg_student_id>/', views.reg_student_details, name='reg_student_details'),
    path('dashboard/sessions/', views.sessions_page, name='sessions_page'),
    path('dashboard/sessions/<int:session_id>', views.sessions_page_main, name='sessions_page_main'),
    path('dashboard/sessions/timer/',views.timer,name="timer")
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)