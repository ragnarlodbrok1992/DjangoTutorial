from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.
# def gameslist(request):
#     return HttpResponse("Hello, world. You're at the gameslist index.")

def gameslist(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='gameslist_landing_page.html',
        context={'adjectives': [s0, s1, 'cool', 'beautiful']}
    )