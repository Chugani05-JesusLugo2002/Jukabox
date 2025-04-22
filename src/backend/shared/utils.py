from django.http import JsonResponse
import json


def check_method(method: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            request = args[0]
            if request.method != method:
                return JsonResponse({'error': 'Method not allowed'}, status=405)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def check_json_body(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        try:
            request.data = json.loads(request.body)
        except:
            return JsonResponse({'error': 'Invalid JSON body'}, status=404)
        return func(*args, **kwargs)
    return wrapper