from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

import requests
from bs4 import BeautifulSoup


# Create your views here.
def home(request):
    if request.method == "POST":
        print(request.POST)
        search_value = request.POST.get("data")
        print("Valor enviado:", search_value)
        return JsonResponse({"hola": "World"})

    else:
        print("No post data")
        return render(request, "home.html")


def valor(request, valor):
    print(valor)
    response = requests.get(f"https://www.google.com/search?q={valor}&tbm=isch")
    soup = BeautifulSoup(response.text, "html.parser")
    image_urls = [img["src"] for img in soup.find_all("img")]
    a = 0
    data = ""
    for url in image_urls:
        print(url)
        data += '<a><img class="img-thumbnail" src="' + url + '" id="' + url + '"></a><button onclick="agregar(\''+url+'\');">agregar</button>'
    
        a += 1
        if a == 6:
            break

    return JsonResponse({"hola":data})