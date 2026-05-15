from django.http import JsonResponse


def home_view(request):
    return JsonResponse({
        "message": "Todo API is running",
        "endpoints": "/api/todos/"
    })