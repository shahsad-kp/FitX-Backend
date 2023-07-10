from django.urls import path

from Messages.views import AllMessagesView

urlpatterns = [
    path('<int:user_id>/', AllMessagesView.as_view())
]
