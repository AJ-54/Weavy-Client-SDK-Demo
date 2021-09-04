from django.shortcuts import render
from django.http import JsonResponse
import jwt
# Create your views here.


def home(request):

    return render(request, "base.html")

def loginView(request):
     if request.method == "GET":

        name = request.GET.get('name')
        # secret key
        key = "buildtomorrow"
        payload = {
            "sub": name,
            "name": name,
            "exp": 2516239022,
            "iss": "buildtomorrow",
        }

        encoded = jwt.encode(payload, key, algorithm="HS256")
        data= {
            "token" : encoded,
        }
        return JsonResponse(data)