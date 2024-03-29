from django.urls import path

from Users.views import CreateUserView, GetUserView, GetSelfUserView, DeleteUserView, UpdateUserView, \
    UpdateSelfUserView, GetAllUsersListView, LikeACategory, DislikeACategory, GetAllLikedCategory, \
    WeightListCreateAPIView, HeightListCreateAPIView, MakePremium

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('get/', GetSelfUserView.as_view()),
    path('get/<int:id>/', GetUserView.as_view()),
    path('getall/', GetAllUsersListView.as_view()),
    path('delete/<int:id>/', DeleteUserView.as_view()),
    path('update/<int:id>/', UpdateUserView.as_view()),
    path('update/', UpdateSelfUserView.as_view()),
    path('like/<int:category_id>/', LikeACategory.as_view()),
    path('dislike/<int:category_id>/', DislikeACategory.as_view()),
    path('getlikes/', GetAllLikedCategory.as_view()),
    path('weight/', WeightListCreateAPIView.as_view()),
    path('height/', HeightListCreateAPIView.as_view()),
    path('premium/', MakePremium.as_view()),
]
