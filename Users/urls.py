from django.urls import path

from Users.views import CreateUserView, GetUserView, GetSelfUserView, DeleteUserView, UpdateUserView, \
    UpdateSelfUserView, GetAllUsersListView, GetUpdateUserGoals

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('get/', GetSelfUserView.as_view()),
    path('get/<int:id>/', GetUserView.as_view()),
    path('getall/', GetAllUsersListView.as_view()),
    path('delete/<int:id>/', DeleteUserView.as_view()),
    path('update/<int:id>/', UpdateUserView.as_view()),
    path('update/', UpdateSelfUserView.as_view())
]

urlpatterns += [
    path('goals/', GetUpdateUserGoals.as_view())
]
