from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from models_app.models import Favorite, Test


@require_POST
@login_required()
def toggle_favorite_ajax(request, test_id):
    """
    Функция переключает тест в избранноe

    @require_POST — допускает только POST-запросы (безопасность).
    @login_required() — только для авторизованных пользователей.
    """
    test = get_object_or_404(Test, id=test_id)

    """
    Пытаемся найти запись в таблице Favorite для текущего пользователя и теста.
    Если находим, переменная fav — это найденная запись, а created = False.
    Если нет, создаём новую запись, и created = True.
    """
    fav, created = Favorite.objects.get_or_create(user=request.user, test=test)

    if not created:
        fav.delete()  # Удалить, если уже было
        # return redirect(request.META.get("HTTP_REFERER", "/"))
        print("[!] toggle_favorite_ajax: ", JsonResponse({"status": "removed"}))
        return JsonResponse({"status": "removed"})
    else:
        print("[!] toggle_favorite_ajax: ", JsonResponse({"status": "added"}))
        return JsonResponse({"status": "added"})
