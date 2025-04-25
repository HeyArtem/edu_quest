from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class ClearSessionMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        self.target_path = reverse("next_question")

    def process_request(self, request):
        current_path = request.path
        previous_path = request.session.get("last_path")

        if previous_path == self.target_path and current_path != self.target_path:
            user = getattr(request, "user", None)
            if user and user.is_authenticated:
                user_session_key = request.session[f"{user.id}_user_session_key"]
                # user_session_key (urls.py) = f"{user.id}_{slug_test}"
                # For Example: "1_math-test"
                session_keys = [
                    f"{user_session_key}_questions",
                    f"{user_session_key}_answers",
                    f"{user_session_key}_total",
                    f"{user.id}_user_session_key",
                ]
                for key in session_keys:
                    del request.session[key]

        request.session["last_path"] = current_path
