from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'portal/login.html', {'error': 'Invalid credentials'})
    return render(request, 'portal/login.html')

@login_required
def home_view(request):
    students = Student.objects.all()
    return render(request, 'portal/home.html', {'students': students})

@login_required
def save_student_ajax(request):
    print(request.POST)
    if request.method == 'POST':
        data = json.loads(request.body)

        name = data.get("name", "").strip()
        subject = data.get("subject", "").strip()

        marks = int(data.get('marks'))

        try:
            student = Student.objects.get( Q(name__iexact=name), Q(subject__iexact=subject))
            student.marks += int(marks)  
            student.subject = data.get('subject')
            student.save()
            return JsonResponse({'status': 'success'})
        except Student.DoesNotExist:
            student = Student.objects.create(name=name, subject=subject, marks=marks)
            student.save()
            return JsonResponse({'status': 'success'})
        # if not created:
        #     student.marks += marks
        # else:
        #     student.marks = marks
        
        


@login_required
def edit_student_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_id = data.get('id')
        student = Student.objects.get(id=student_id)
        student.name = data['name']
        student.subject = data['subject']
        student.marks = data['marks']
        student.save()
        return JsonResponse({'status': 'updated'})


@login_required
def delete_student_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Student.objects.filter(id=data['id']).delete()
        return JsonResponse({'status': 'deleted'})