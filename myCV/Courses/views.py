from django.shortcuts import render


def courses(request):
    context = {
        'title': 'Courses',
    }
    return render(request, 'Courses/courses.html', context)
