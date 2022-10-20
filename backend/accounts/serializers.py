from djoser.serializers import UserCreateSerializer

from djoser.serializers import UserSerializer

class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'first_name', 'balance', 'username', 'password', )


class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('email', 'first_name', 'balance', 'username', )
