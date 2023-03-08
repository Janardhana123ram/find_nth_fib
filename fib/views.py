import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Fibonacci
from fib.serializers import FibonacciSerializer

def fibonacci_series(n):   
    if n < 0:  
        print("Oops! Incorrect input")  
    elif n == 0:   
        return (0)   
    elif n == 1:  
        return (1)  
    else:  
        return (fibonacci_series(n - 1) + fibonacci_series(n - 2))

def create_fibonacci(nth_value):
    fib_value = fibonacci_series(nth_value)
    fib_cursor = Fibonacci(n=nth_value, nth=fib_value, status = "success")
    fib_cursor.save()
    return fib_value

def prepare_data(data):
    data.pop("n")
    data["nth"] = str(data["nth"])
    return data

@csrf_exempt
def fibonacci_list(request):

    if request.method == "GET":
        fibs = Fibonacci.objects.all()
        serializer = FibonacciSerializer(fibs, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def fibonacci_detail(request):
    
    n = json.loads(request.body)["n"]
    if request.method == "POST":
        try:
            fib_value = Fibonacci.objects.get(n=n)
            serializer = FibonacciSerializer(fib_value)
            data = prepare_data(serializer.data)
            return JsonResponse(data)
        except Fibonacci.DoesNotExist:
            fib_value = create_fibonacci(n)
            fib_value = Fibonacci.objects.get(n=n)
            serializer = FibonacciSerializer(fib_value)
            data = prepare_data(serializer.data)
            return JsonResponse(data)
