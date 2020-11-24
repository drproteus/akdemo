from django.conf import settings

def util(request):
    return {
        "current_user": request.user,
        "is_authenticated": request.user.is_authenticated,
        "umami_url": settings.UMAMI_URL,
        "umami_token": settings.UMAMI_TOKEN
    }
