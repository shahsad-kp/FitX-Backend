from rest_framework.serializers import ModelSerializer

from Banner.models import Banner


class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
