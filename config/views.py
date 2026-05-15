from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Todo API is running",
        "endpoints": "/api/todos/"
    })