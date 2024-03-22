from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse 
from .forms import CourseForm  
from .models import Course 
# Create your views here.  


def course_list(request):  # Get all the course from the table
    course_list =  Course.objects.all()  
    return render(request, 'courses/course_list.html', {
        'course_list':course_list,
    })

def create_course(request):  # Can edit seleted course
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('course_list')  # Redirect to the all list of the course
    else:
        form = CourseForm()
    return render(request, 'courses/create.html', {'form': form})  # render to the create course page


def update_course(request, course_id): # Can update seleted course
    course_role = get_object_or_404(Course, pk=course_id) 
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course_role)  
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course_role)  
    return render(request, 'courses/update.html', {'form': form})  # render to the update course page


def delete_course(request, course_id):  # Can delete seleted course
    course_role = Course.objects.get(pk=course_id) 
    if request.method == 'POST':
        course_role.delete() 
        return redirect('course_list')
    
    return render(request, 'courses/delete.html', {'course_role':course_role})  # render to the delete course page