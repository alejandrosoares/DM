from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('', include("home.urls")),
    path('contact', include("contact.urls")),
    path('products/', include("products.urls")),
    path('chat/', include("chat.urls")),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
