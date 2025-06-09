from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from conf.settings import django
from edu_quest.views.handler import Handler404View

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("edu_quest.urls")),
    path("_nested_admin/", include("nested_admin.urls")),
]

handler404 = Handler404View.as_view()

if django.DEBUG:
    urlpatterns += static(django.STATIC_URL, document_root=django.STATIC_ROOT)
    urlpatterns += static(django.MEDIA_URL, document_root=django.MEDIA_ROOT)

if django.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
