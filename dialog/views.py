from django.shortcuts import render

# Create your views here.

def dialog_index(request):
    return render(request, 'dialog/index.html')
