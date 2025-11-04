from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/gestion/cursos/', permanent=True), name='inicio'),
    path('gestion/cursos/', include('apps.modulo_3.cursos.urls', namespace='cursos')),
    path('gestion/docentes/', include('apps.modulo_3.docentes.urls', namespace='docentes')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)