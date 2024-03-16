from django.shortcuts import render

# Create your views here.
from .models import Student, Degree

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_degrees/student_list.html', {'students': students})

def degree_list(request):
    degrees = Degree.objects.all()
    return render(request, 'student_degrees/degree_list.html', {'degrees': degrees})
