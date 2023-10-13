from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import maps.urls
import products.urls
from settings import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/', include(maps.urls.pages_urls)),
    path('api/v1/maps/', include(maps.urls.api_urls)),
    path('api/v1/products/', include(products.urls.api_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
