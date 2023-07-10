from rest_framework.serializers import ModelSerializer

from Users.models import User, Height, Weight


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'profile_picture',
            'username',
            'date_of_birth',
            'email',
            'gender',
            'password',
            'is_trainer',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User(  # Assign the newly created UserData instance to the user_data field
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user


class WeightSerializer(ModelSerializer):
    class Meta:
        model = Weight
        fields = ['date', 'weight']
        read_only_fields = ['user', 'date']

    def create(self, validated_data):
        user = self.context['request'].user
        weight = validated_data['weight']
        return Weight.objects.create(user=user, weight=weight)


class HeightSerializer(ModelSerializer):
    class Meta:
        model = Height
        fields = ['date', 'height']
        read_only_fields = ['user', 'date']

    def create(self, validated_data):
        user = self.context['request'].user
        height = validated_data['height']
        return Height.objects.create(user=user, height=height)
