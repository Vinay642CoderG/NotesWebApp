from django.http.response import FileResponse
from django.http import HttpResponseForbidden, HttpResponse
from notespr.settings import MEDIA_ROOT
import os
# Create your views here.

def media_access(request, user_id, filename):    
    access_granted = False

    user = request.user
    if user.user_id==user_id or user.is_staff:
        access_granted = True
    else:
        access_granted = False
    
    if access_granted:
        file_path = os.path.join(MEDIA_ROOT, "profile", filename)
        # Check if the file exists
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'))
            return response
        else:
            return HttpResponse("File not found", status=404)
    else:
        return HttpResponseForbidden("Not authorized to access this media.")

