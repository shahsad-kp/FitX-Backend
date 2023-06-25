from django.urls import path

from Goals.views import WeeklyExerciseGoalCreateUpdateRetrieveAPIView, GetAllExerciseGoals, GetAllCategoryGoals, \
    GetAllCalorieGoals, WeeklyCategoryGoalCreateUpdateRetrieveAPIView, WeeklyCalorieGoalCreateUpdateRetrieveAPIView

urlpatterns = [
    path('calorie/', WeeklyCalorieGoalCreateUpdateRetrieveAPIView.as_view()),
    path('category/', WeeklyCategoryGoalCreateUpdateRetrieveAPIView.as_view()),
    path('exercise/', WeeklyExerciseGoalCreateUpdateRetrieveAPIView.as_view()),
    path('exercise/all/', GetAllExerciseGoals.as_view()),
    path('category/all/', GetAllCategoryGoals.as_view()),
    path('calorie/all/', GetAllCalorieGoals.as_view())
]
