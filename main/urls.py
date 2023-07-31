from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', SpectacularSwaggerView.as_view(), name="swagger"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('', include('app.urls'))
]
