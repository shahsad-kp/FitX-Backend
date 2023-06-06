from django.urls import path

from Exercises.views import CreateCategoryView, GetCategoryView, GetAllCategoriesView, UpdateCategoryView

urlpatterns = [
    path('exercise/getall/', GetAllCategoriesView.as_view()),
    path('exercise/create/', CreateCategoryView.as_view()),
    path('exercise/get/<int:id>/', GetCategoryView.as_view()),
    path('exercise/update/<int:id>/', UpdateCategoryView.as_view()),
]
