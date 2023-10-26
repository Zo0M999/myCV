from django.shortcuts import render


def aboutMe(request):
    context = {
        'title': 'AboutMe',
    }
    return render(request, 'AboutMe/aboutMe.html', context)
