from django.urls import path

from Category.views import GetAllCategoriesView, CreateCategoryView, GetCategoryView, UpdateCategoryView

urlpatterns = [
    path('getall/', GetAllCategoriesView.as_view()),
    path('create/', CreateCategoryView.as_view()),
    path('get/<int:id>/', GetCategoryView.as_view()),
    path('update/<int:id>/', UpdateCategoryView.as_view()),
]
