from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from Transformation.models import TransformationImage
from Transformation.serializers import TransformationImageSerializer


class TransformationImageView(ListCreateAPIView):
    serializer_class = TransformationImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: TransformationImageSerializer):
        serializer.initial_data['user'] = self.request.user
        return super().perform_create(serializer)

    def get_queryset(self):
        return TransformationImage.objects.all().filter(user=self.request.user)


class DeleteTransformationImageView(DestroyAPIView):
    serializer_class = TransformationImageSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        transformation_image = TransformationImage.objects.get(id=self.kwargs['id'])
        if transformation_image.user != self.request.user:
            raise PermissionError('You are not allowed to delete this object')
        return transformation_image

