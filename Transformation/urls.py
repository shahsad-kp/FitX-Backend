from django.urls import path

from Transformation.views import TransformationImageView, DeleteTransformationImageView

urlpatterns = [
    path('', TransformationImageView.as_view()),
    path('delete/<int:id>/', DeleteTransformationImageView.as_view(), name='delete_transformation_image')
]
