from django.shortcuts import render, redirect
from django.views import View

from . import models

# Create your views here.

class DialogView(View):
    def get(self, request):
        mensagens = models.DialogMessage.objects.all()

        return render(request, 'dialog/index.html', context={
            'messages': mensagens
        })
    
    def post(self, request):
        mensagem = request.POST.get('mensagem')

        if not mensagem:
            return redirect('dialog_view')
        
        models.DialogMessage.objects.bulk_create((
            models.DialogMessage(type=1, message=mensagem),
            models.DialogMessage(type=2, message=f'respondendo a mensagem: {mensagem}')
        ))
        
        return redirect('dialog_view')
