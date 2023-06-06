from django.urls import path

from Users.views import CreateUserView, GetUserView, GetSelfUserView, DeleteUserView, UpdateUserView, UpdateSelfUserView

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('get/', GetSelfUserView.as_view()),
    path('get/<int:id>/', GetUserView.as_view()),
    path('delete/<int:id>/', DeleteUserView.as_view()),
    path('update/<int:id>/', UpdateUserView.as_view()),
    path('update/', UpdateSelfUserView.as_view())
]
