from django.urls import path

from Banner.views import AddBanner, DeleteBanner, ListBanners

urlpatterns = [
    path('add/', AddBanner.as_view()),
    path('delete/<int:id>/', DeleteBanner.as_view()),
    path('/', ListBanners.as_view())
]
