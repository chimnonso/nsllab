# middleware.py
from django.utils import timezone
from django.contrib.auth import logout
from django.conf import settings

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity_str = request.session.get('last_activity', None)
            if last_activity_str:
                last_activity = timezone.datetime.fromisoformat(last_activity_str)
                if (timezone.now() - last_activity).seconds > settings.AUTO_LOGOUT_TIME:
                    logout(request)
                else:
                    request.session['last_activity'] = timezone.now().isoformat()
            else:
                request.session['last_activity'] = timezone.now().isoformat()

        response = self.get_response(request)
        return response
