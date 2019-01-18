from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'chatapp/index.html')


def temp(request):
    return HttpResponse("You are at the temperature now.")

def bot(request):
    # Get the request content, give back the information
    # Population, temperature today or tomorrow
    if request.method == "POST":
        response = 'I do not understand'
        data = request.POST
        userinput = data['input'].strip()
        greeting = ['hi', 'hello']
        try:
            response = str(ChatInfo.objects.get(question=userinput)) # dbquery(userinput)
        except ObjectDoesNotExist as oe:
            print(oe)
            # response = oe.__str__()
            response = "Default message"
        except Exception as e:
            print(e)
            response = "Default message"
        print(response)
        if userinput in greeting:
            response = "Hi there!"
        elif userinput == "how are you?":
            response = "I'm fine, thanks!"
        return JsonResponse({'reply': response})
    else :
        return render(request, 'chatapp/bot.html')