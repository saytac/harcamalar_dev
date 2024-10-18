from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.sessions.models import Session
from django.utils import timezone

User = get_user_model()


class SingleSessionBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if user:
            # Delete all existing sessions for this user
            Session.objects.filter(expire_date__gte=timezone.now(),
                                   session_data__contains=str(user.id)).delete()
        return user
