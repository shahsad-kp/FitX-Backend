from django.urls import path

from Transformation.views import TransformationImageView

urlpatterns = [
    path('', TransformationImageView.as_view())
]
