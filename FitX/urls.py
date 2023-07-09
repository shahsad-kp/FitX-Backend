from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation for FitX",
        default_version='v1',
        contact=openapi.Contact(email="shahsadkpklr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('UserAuth.urls')),
    path('users/', include('Users.urls')),
    path('category/', include('Category.urls')),
    path('exercise/', include('Exercises.urls')),
    path('banner/', include('Banner.urls')),
    path('goals/', include('Goals.urls')),
    path('trainer/', include('Trainer.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
