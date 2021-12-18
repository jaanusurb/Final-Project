from django.shortcuts import render


def home(request):
    request.session['name'] = 'User'
    username = request.session['name']

    return render(request, 'home.html', context={'username': username})