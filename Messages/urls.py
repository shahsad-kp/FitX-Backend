from django.urls import path

from Messages.views import AllMessagesView, AllMessagedUsersView

urlpatterns = [
    path('<int:user_id>/', AllMessagesView.as_view()),
    path('users/', AllMessagedUsersView.as_view()),
]
