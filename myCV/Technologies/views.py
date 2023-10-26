from django.shortcuts import render


def technologies(request):
    context = {
        'title': 'Technologies',
    }
    return render(request, 'Technologies/technologies.html', context)
