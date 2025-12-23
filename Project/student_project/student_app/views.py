from django.shortcuts import get_object_or_404, redirect, render
from student_app.models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            student_id = int(request.POST.get('student_id')),
            full_name = request.POST.get('full_name'),
            department = request.POST.get('department'),
            dob = request.POST.get('dob'),
            gender = request.POST.get('gender'),
            address = request.POST.get('address'),
            image = request.FILES.get('image')
        )
        return redirect('show_student')
    return render(request, 'student/add_student.html')

def show_student(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student/show_student.html', context)

def update_student(request, id):
    student = get_object_or_404(Student, id = id)
    context = {
        'student' : student
    }
    if request.method == "POST":
        student.student_id = int(request.POST.get('student_id'))
        student.full_name = request.POST.get('full_name')
        student.department = request.POST.get('department')
        student.dob = request.POST.get('dob')
        student.gender = request.POST.get('gender')
        student.address = request.POST.get('address')
        user_image = request.FILES.get('image')
        if user_image:
            student.image = user_image

        student.save()
        return redirect('show_student')

    return render(request, 'student/update_student.html', context)

def delete_student(request, id):
    student = Student.objects.filter(id=id)
    student.delete()
    return redirect('show_student')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("envalid password")

    return render(request, 'auth/user_login.html')


def sign_up(request):
    if request.method == "POST":
        User.objects.create_user(
            username = request.POST.get('username'),
            email = request.POST.get('email'),
            password = request.POST.get('password')
           
        )
        return redirect('user_login')
    return render(request, 'auth/sign_up.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')




