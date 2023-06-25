from django.urls import path

from Goals.views import WeeklyCalorieGoalViewSet, WeeklyCategoryGoalViewSet, WeeklyExerciseGoalViewSet, \
    GetAllExerciseGoals, GetAllCategoryGoals, GetAllCalorieGoals

urlpatterns = [
    path('calorie/', WeeklyCalorieGoalViewSet.as_view()),
    path('category/', WeeklyCategoryGoalViewSet.as_view()),
    path('exercise/', WeeklyExerciseGoalViewSet.as_view()),
    path('exercise/all/', GetAllExerciseGoals.as_view()),
    path('category/all/', GetAllCategoryGoals.as_view()),
    path('calorie/all/', GetAllCalorieGoals.as_view())
]
