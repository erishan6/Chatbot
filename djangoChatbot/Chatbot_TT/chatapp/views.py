from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from random import *
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
        try:
            response = str(ChatInfo.objects.get(question=userinput))
            if "|" in response:
                ans = response.strip().split("|")
                print(ans)
                index = randint(0, len(ans)-1)
                response=ans[index]

        except ObjectDoesNotExist as oe:
            print(oe)
            # response = oe.__str__()
            response = "Answer not found in db. Try a internet search"
            # response = 'I do not understand'
        except Exception as e:
            print(e)
            # response = "Answer not found in db. Try a internet search"
            response = 'I do not understand'
        print(response)
        return JsonResponse({'reply': response})
    else :
        return render(request, 'chatapp/bot.html')