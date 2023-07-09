from django.urls import path

from .views import ApplyForTrainerView, CertificateView, RespondToTrainerApplicationView, TrainerListView, \
    TrainerApplicationsListView

urlpatterns = [
    path('apply/', ApplyForTrainerView.as_view(), name='apply-for-trainer'),
    path('certificate/', CertificateView.as_view(), name='upload-certificate'),
    path('respond/<int:trainer_id>/', RespondToTrainerApplicationView.as_view(), name='respond-to-trainer-application'),
    path('all/', TrainerListView.as_view(), name='trainer-list'),
    path('applications/', TrainerApplicationsListView.as_view(), name='trainer-applications-list')
]
