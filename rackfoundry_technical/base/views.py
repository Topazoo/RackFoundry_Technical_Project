from django.shortcuts import render

def home(request):
    ''' Render the main homepage '''
    return render(request, 'base/home.html', {})

def marvel_home(request):
    ''' Render the marvel homepage '''
    return render(request, 'base/marvel_home.html', {})

def tickets_home(request):
    ''' Render the tickets homepage '''
    return render(request, 'base/tickets_home.html', {})