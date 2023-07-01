from django.urls import path

from Category.views import GetAllCategoriesView, CreateCategoryView, GetCategoryView, UpdateCategoryView, \
    AddExerciseIntoCategory, DeleteCategoryView, RemoveExerciseFromCategory, GetCategoryLikes, CompletedCategoryView

urlpatterns = [
    path('getall/', GetAllCategoriesView.as_view()),
    path('create/', CreateCategoryView.as_view()),
    path('get/<int:id>/', GetCategoryView.as_view()),
    path('update/<int:id>/', UpdateCategoryView.as_view()),
    path('<int:category_id>/add/<int:exercise_id>/', AddExerciseIntoCategory.as_view()),
    path('<int:category_id>/remove/<int:exercise_id>/', RemoveExerciseFromCategory.as_view()),
    path('<int:category_id>/likes/', GetCategoryLikes.as_view()),
    path('delete/<int:id>/', DeleteCategoryView.as_view()),
    path('completed/', CompletedCategoryView.as_view()),
]
