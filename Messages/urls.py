from django.urls import path

from Messages.views import AllMessagesView, AllMessagedUsersView, UploadMessageImage

urlpatterns = [
    path('<int:user_id>/', AllMessagesView.as_view()),
    path('users/', AllMessagedUsersView.as_view()),
    path('upload/', UploadMessageImage.as_view()),
]
