import random

from django.shortcuts import render

# Create your views here.
def lotto(request):

    result = []

    for i in range(6):
        result.append(random.randint(1, 46))

    return render(request, "lotto.html", {"result": result})
