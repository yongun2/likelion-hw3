from django.http import HttpResponse
from django.shortcuts import render


def calculator(request):
    # 1. 데이터 확인
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    operators = request.GET.get("operators")

    # 2. 계산
    if operators == "+":
        result = int(num1) + int(num2)
    elif operators == "-":
        result = int(num1) - int(num2)
    elif operators == "*":
        result = int(num1) * int(num2)
    elif operators == "/":
        result = int(num1) / int(num2)
    else:
        result = 0

    # 3. 응답

    return render(request, "calculator.html", {"result": result})
