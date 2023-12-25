import csv
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from insb_spac import settings
from main.forms import CSVImportForm

from main.models import Meeting_Session, Meeting_Session_FeedBack_Link, Meeting_Session_Files, Reg_Student, Reg_Student_Attendance, Reg_Student_Items

# Create your views here.

def login_page(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if(user is not None):
            auth.login(request, user)
            return redirect('main:dashboard')
        else:
            messages.error(request, "Credentials don't match")

    return render(request, 'login.html')

def signup_page(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if(confirm_password == password):
            if(User.objects.filter(username=username).exists()):
                messages.error(request, "User already exists")
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()

                messages.success(request, "Account Created Successfully")
                return redirect('main:login_page')
        else:
            messages.error(request,"Two Passwords do not match")
    
    return render(request, 'signup.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('main:login_page')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def import_csv(request):
    form = CSVImportForm(request.POST, request.FILES)
    if form.is_valid():
        csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            student = Reg_Student.objects.create(
                name=row['Name'],
                email=row['Email'],
                ieee_id=row['IEEE ID'],
                university=row['University Name'],
                department=row['University Department Name'],
                university_id=row['University ID'],
                picture_link=row['Attach your picture here'],
                reference=row['Reference (Ambassador Unique Code):'],
                t_shirt_size=row['T-Shirt size:'],
                transaction_id=row['Transaction ID_1']+row['Transaction ID_2']+row['Transaction ID_3']
            )

            student_items = Reg_Student_Items.objects.create(student=student)
            student_items.save()
        
        return redirect('main:dashboard')
    else:
        form = CSVImportForm()
    
    return render(request, 'csv.html', {'form': form})

@login_required
def reg_students(request):
    reg_students = Reg_Student.objects.all()

    return render(request, 'reg_students.html', {'reg_students' : reg_students})

@login_required
def reg_student_details(request, reg_student_id):
    student = Reg_Student.objects.get(id=reg_student_id)
    student_items = Reg_Student_Items.objects.get(student=student)

    if request.method == 'POST':
        t_shirt = False
        if request.POST.get('t_shirt'):
            t_shirt = True

        goodies = False
        if request.POST.get('goodies'):
            goodies = True

        certificate = False
        if request.POST.get('certificate'):
            certificate = True

        student_items.t_shirt = t_shirt
        student_items.goodies = goodies
        student_items.certificate = certificate
        student_items.save()
        messages.success(request, 'wsdfghjgfdsa')
    
    context = {
        'student' : student,
        'student_items' : student_items,
        'reg_student_id' : reg_student_id
    }
    
    return render(request, 'reg_student_details.html', context)

@login_required
def reg_students_attendance(request):
    sessions = Meeting_Session.objects.all()

    return render(request, 'reg_students_attendance.html', {'sessions' : sessions})

@login_required
def reg_students_attendance_main(request, session_id):
    
    session = Meeting_Session.objects.get(pk=session_id)
    students_attendance = Reg_Student_Attendance.objects.filter(session=session)

    attendance_count = 0
    for student in students_attendance:
        if student.attendance == True:
            attendance_count += 1

    if request.method == 'POST':
        if('update_attendance' in request.POST):
            attendances = request.POST.getlist('attendance')

            for student in students_attendance:
                print(student.student)
                if str(student.student) in attendances:
                    Reg_Student_Attendance.objects.filter(student=student.student, session=session).update(attendance=True)
                else:
                    Reg_Student_Attendance.objects.filter(student=student.student, session=session).update(attendance=False)

            return redirect('main:reg_students_attendance_main', session_id)
        elif('get_students' in request.POST):
            session = Meeting_Session.objects.get(pk=session_id)
            if(Reg_Student_Attendance.objects.filter(session=session).count() > 0):
                return redirect('main:reg_students_attendance_main', session_id)
            students = Reg_Student.objects.all()

            for student in students:
                attendance = Reg_Student_Attendance.objects.create(student=student, session=session)
                attendance.save()
            return redirect('main:reg_students_attendance_main', session_id)
        elif('remove_students' in request.POST):
            if(Reg_Student_Attendance.objects.filter(session=session).count() > 0):
                Reg_Student_Attendance.objects.filter(session=session).delete()
                return redirect('main:reg_students_attendance_main', session_id)
            else:
                return redirect('main:reg_students_attendance_main', session_id)

    context = {
        'session': session,
        'students_attendance': students_attendance,
        'total_students' : students_attendance.count(),
        'attendance_count' : attendance_count
    }
    return render(request, 'reg_students_attendance_main.html', context)

@login_required
def sessions_page(request):
    sessions = Meeting_Session.objects.all()

    return render(request, 'sessions_page.html', {'sessions' : sessions})

def sessions_page_main(request, session_id):
    session = Meeting_Session.objects.get(id=session_id)

    if request.method == 'POST':
        if 'timer_link' in request.POST:
            return redirect('main:timer', request.POST['form_link'])

    feedback_link = Meeting_Session_FeedBack_Link.objects.get(session=session)
    all_graphic_files = Meeting_Session_Files.objects.filter(session=session)
    context = {
        'media_url' : settings.MEDIA_URL,
        'session_id' : session_id,
        'session' : session,
        'feedback_link' : feedback_link,
        'all_graphic_files' : all_graphic_files
    }

    return render(request, 'sessions_page_main.html', context)

def timer(request):
    return render(request,"timer.html")
