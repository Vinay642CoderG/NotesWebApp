# context_processors.py
def myglobal_context(request):
    context_data = {
        'user': request.user,
    }
    return context_data
