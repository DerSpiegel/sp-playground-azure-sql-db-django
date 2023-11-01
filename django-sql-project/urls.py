from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

#URl patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customerapi/', include('customerapi.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)