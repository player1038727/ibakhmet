from django.shortcuts import render
from django.http import HttpResponse
import requests


#from .models import Greeting

# Create your views here.
def x(request):
    # return HttpResponse('Hello from Python!')
    m = 'm'
    u = 'u'
    r = requests.post("https://discord.com/api/webhooks/922904892031524864/7HK6lO9sAJBm4unBnI8CaTmewdGxml3Y4bgj1xhOAsAygW4DFrcHZQsvInZfvlRvwR8y", data={'content': m, 'username': u, 'avatar_url': r'https://assets.stickpng.com/images/580b57fcd9996e24bc43c540.png'})

    if r.status_code == '204':
        context = {'responce': '@'+u+', спасибо, записал!'}
    elif m == '':
        context = {'responce': '@'+u+', ошибка: нужно ввести текст, который произнес стример (в одном сообщении, после команды)'}
    else:
        context = {'responce': 'Error'}

    return render(request, "x.html", context)


