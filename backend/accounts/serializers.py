from rest_framework import serializers

from djoser.serializers import UserCreateSerializer
from djoser.serializers import UserSerializer

from .models import Transactions


class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            'email',
            'first_name',
            'balance',
            'username',
            'password',
            )


class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('email',
                  'first_name',
                  'balance',
                  'username',
                  )

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = (
            'amount',
            'type',
            'created_at',
        )
