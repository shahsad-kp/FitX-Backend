from django.urls import path

from Exercises.views import CreateExercise, GetExercise, UpdateExercise, DeleteExercise, GetListAllExercise

urlpatterns = [
    path('create/', CreateExercise.as_view()),
    path('get/<int:id>/', GetExercise.as_view()),
    path('update/<int:id>/', UpdateExercise.as_view()),
    path('delete/<int:id>/', DeleteExercise.as_view()),
    path('getall/', GetListAllExercise.as_view())
]
