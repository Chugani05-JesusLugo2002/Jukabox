from django.http import JsonResponse
import json
import re

from users.models import Profile

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

def assert_body_fields(*fields: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            request = args[0]
            for field in fields:
                if field not in request.data:
                    return JsonResponse({'error': 'Missing required fields'}, status=400)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def assert_token(func):
    def wrapper(*args, **kwargs):
        TOKEN_PATTERN = r'^Bearer ([a-fA-F\d]{8}(?:\-[a-fA-F\d]{4}){3}\-[a-fA-F\d]{12})$'
        request = args[0]
        auth_header = request.headers.get('Authorization')
        if token := re.match(TOKEN_PATTERN, auth_header):
            try:
                request.profile = Profile.objects.get(token=token[1])
            except Profile.DoesNotExist:
                return JsonResponse({'error': 'Unregistered authentication token'}, status=401)
        else:
            return JsonResponse({'error': 'Invalid authentication token'}, status=400)
        return func(*args, **kwargs)

    return wrapper