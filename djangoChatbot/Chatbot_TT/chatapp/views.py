from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'chatapp/index.html')


def temp(request):
    return HttpResponse("You are at the temperature now.")

def bot(request):
    # Get the request content, give back the information
    # Population, temperature today or tomorrow
    print(request, " 11111111111111111111111")
    if request.method == "POST":
        response = 'I do not understand'
        data = request.POST
        userinput = data['input'].strip().lower()
        print(userinput, " 222222222222222222")
        greeting = ['hi', 'hello']
        response = str(ChatInfo.objects.filter(question=userinput))
        print(response)

        if userinput in greeting:
            response = "Hi there!"
        elif userinput == "how are you?":
            response = "I'm fine, thanks!"
        # elif 'stuttgart' in userinput and 'temperature' in userinput:
        #     response = 'The temperature in Stuttgart today is ' + str(ChatInfo.objects.filter(question='Stuttgart')[0].temp_today) + ' degree.'
        return JsonResponse({'reply': response})
    else :
        return render(request, 'chatapp/bot.html')