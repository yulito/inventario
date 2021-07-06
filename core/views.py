from django.shortcuts import render

def index(request):
    print('estoy en el index')
    context ={}
    return render(request, 'core/index.html', context)
