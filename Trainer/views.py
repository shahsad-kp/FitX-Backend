from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from Trainer.models import TrainerData
from Trainer.serializers import TrainerSerializer, CertificateSerializer, TrainerListSerializer


class ApplyForTrainerView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TrainerSerializer

    def create(self, request, *args, **kwargs):
        try:
            trainer_data = request.user.trainer_data
            response = {
                'detail': 'You already applied for trainer.',
                'trainer_data': TrainerSerializer(trainer_data).data
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except TrainerData.DoesNotExist:
            pass
        if request.user.is_trainer:
            response = {
                'detail': 'You are already a trainer.'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class CertificateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CertificateSerializer


class RespondToTrainerApplicationView(GenericAPIView):
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        trainer_id = kwargs.get('trainer_id')
        trainer = TrainerData.objects.get(id=trainer_id)
        response = request.data.get('response')
        if response == 'accept':
            trainer.user.is_trainer = True
            trainer.user.save()
            return Response({'detail': 'Trainer accepted.'}, status=status.HTTP_200_OK)
        elif response == 'reject':
            trainer.delete()
            return Response({'detail': 'Trainer rejected.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid response.'}, status=status.HTTP_400_BAD_REQUEST)


class TrainerListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TrainerListSerializer

    def get_queryset(self):
        queryset = TrainerData.objects.filter(user__is_trainer=True).select_related('user')
        return queryset


class TrainerApplicationsListView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TrainerListSerializer

    def get_queryset(self):
        queryset = TrainerData.objects.filter(user__is_trainer=False).select_related('user')
        return queryset
