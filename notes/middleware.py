from django.conf import settings
from django.http import HttpResponseForbidden

class MediaAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is for a media file and the user is not authenticated

        if request.path.startswith(settings.MEDIA_URL) and not request.user.is_authenticated and not request.user.is_staff:
            return HttpResponseForbidden("Access to media files is restricted.")

        return self.get_response(request)
