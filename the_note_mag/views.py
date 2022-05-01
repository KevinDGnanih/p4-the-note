from django.shortcuts import render

def home_page(request):
    return render(request, 'p4-the-note/templates/home_page')

