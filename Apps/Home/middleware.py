from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.public_urls = getattr(settings, 'PUBLIC_URLS', [])

    def __call__(self, request):
        if not request.user.is_authenticated:
            current_path = request.path
            is_public = any(current_path.startswith(url) for url in self.public_urls)
            if not is_public:
                return redirect(reverse('home:Login'))
        
        response = self.get_response(request)
        return response