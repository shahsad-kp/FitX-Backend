
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
    path('category/', include('Category.urls')),
    path('banner/', include('Banner.urls'))
]
