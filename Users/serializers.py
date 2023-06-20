import datetime

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
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        height = validated_data.pop('height', 0)
        weight = validated_data.pop('weight', 0)

        user = User(  # Assign the newly created UserData instance to the user_data field
            **validated_data
        )
        user.set_password(password)
        user.save()

        Height.objects.create(
            date=datetime.datetime.utcnow(),
            height=height,
            user_data=user
        )
        Weight.objects.create(
            date=datetime.datetime.utcnow(),
            weight=weight,  # Fixed typo: use 'weight' instead of 'height'
            user_data=user
        )
        return user


class GoalsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'weekly_calorie_goal', 'weekly_category_goal', 'weekly_exercise_goal']
