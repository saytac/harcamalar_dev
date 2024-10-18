from django.contrib.sessions.models import Session
from django.contrib.auth import logout
from django.utils import timezone
from django.contrib import messages


class SingleSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_session_key = request.session.session_key
            user_sessions = Session.objects.filter(
                expire_date__gte=timezone.now(),
                session_data__contains=str(request.user.id)
            ).exclude(session_key=current_session_key)
            if user_sessions.exists():
                user_sessions.delete()
                logout(request)
                messages.warning(request, 'You have been logged out because you logged in from another device.')

        response = self.get_response(request)
        return response



