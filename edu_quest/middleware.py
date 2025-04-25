from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from conf.settings.django import MEDIA_URL, STATIC_URL


class ClearSessionMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        # Путь куда сейчас пойдем, путь цель
        self.target_path = reverse("next_question")

    def process_request(self, request):
        current_path = request.path

        # Когда загружается страница с тестом, то автоматически
        # делается get-запрос для подгрцзки медиа, нужно это игнорировать (выдти из функции)
        # if current_path.startswith(("/media/", "/static/")):
        #     return

        if current_path.startswith((MEDIA_URL, STATIC_URL)):
            return

        previous_path = request.session.get("last_path")

        print(
            f"previous_path:{previous_path} | current_path:{current_path} | target_path:{self.target_path}"
        )

        """
                                 названия маршрутов
        Всегда: target_path ('next_question')

                                 преду-щий            текущий
                            previous_path    -->    current_path
Заходит на страницу вопроса	   None	                  /next_question/   ❌ Нет Очистки
Переходит на другой вопрос	  /next_question/	       /next_question/  ❌ Нет Очистки
Переходит на главную страницу	/next_question/	       /home/        	✅ Да Очистка
Открывает результаты теста  	/next_question/	      /user_result/  	✅ Да Очистка

        """

        # Очистка сессии Если: предыдущая стр была вопросом И сейчас не на стр вопроса ->
        if previous_path == self.target_path and current_path != self.target_path:
            # # Чистка ссесии
            # request.session.flush()
            # Получаю из request-> user, подстраховочный вар, через getattr
            user = getattr(request, "user", None)
            if user and user.is_authenticated:
                user_session_key = request.session[f"{user.id}_user_session_key"]

                # Список переменных в сесии, которые я буду очищать
                session_keys = [
                    f"{user_session_key}_questions",
                    f"{user_session_key}_answers",
                    f"{user_session_key}_total",
                    f"{user.id}_user_session_key",
                ]
                for key in session_keys:
                    del request.session[key]

        request.session["last_path"] = current_path
