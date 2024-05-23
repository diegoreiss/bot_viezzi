from django.shortcuts import render, redirect
from django.views import View

from . import models
import services.bot

# Create your views here.

class DialogView(View):
    def get(self, request):
        mensagens = models.DialogMessage.objects.all()



        return render(request, 'dialog/index.html', context={
            'messages': mensagens
        })
    
    def post(self, request):
        esperando_clima = False
        mensagem = request.POST.get('mensagem')

        if not mensagem:
            return redirect('dialog_view')

        last_message = models.DialogMessage.objects.all().last()
        if not last_message:
            esperando_clima = False
        
        if last_message and 'cidade' in last_message.message.split():
            esperando_clima = True
        
        resposta = services.bot.viezzi_init(mensagem, esperando_clima)
        print(resposta)

        if isinstance(resposta, list):
            models.DialogMessage.objects.create(type=1, message=mensagem)
            models.DialogMessage.objects.bulk_create([
                models.DialogMessage(type=2, message=m) for m in resposta
            ])
        else:
            
            models.DialogMessage.objects.bulk_create((
                models.DialogMessage(type=1, message=mensagem),
                models.DialogMessage(type=2, message=resposta)
            ))
        
        return redirect('dialog_view')
