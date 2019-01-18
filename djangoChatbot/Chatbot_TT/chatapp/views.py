from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

# View for chatapp index page
def index(request):
    return render(request, 'chatapp/index.html')

# View for bot page
def bot(request):
    # Get the request content, give back the information
    if request.method == "POST":
        response = 'I do not understand'
        data = request.POST
        userinput = data['input'].strip().lower()
        greeting = ['hi', 'hello']
        try:
            response = str(ChatInfo.objects.get(question=userinput))
        except ObjectDoesNotExist as oe:
            print(oe)
            # response = oe.__str__()
            response = "Answer not found in db. Try a internet search"
        except Exception as e:
            print(e)
            response = "Answer not found in db. Try a internet search"
        print(response)
        if userinput in greeting:
            response = "Hi there!"
        elif userinput == "how are you?":
            response = "I'm fine, thanks!"
        return JsonResponse({'reply': response})
    else :
        return render(request, 'chatapp/bot.html')