from django.contrib.auth.models import User, Group
from .models import Client, CurrencyType, Account, Transfer
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'password')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    accounts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Client
        fields = ('id', 'user', 'firstname', 'lastname', 'idcard', 'phone', 'accounts')


class CurrencyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CurrencyType
        fields = ('id', 'name', 'symbol')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=False)
    currencyType = serializers.PrimaryKeyRelatedField(queryset=CurrencyType.objects.all(), many=False)
    currency = serializers.StringRelatedField(many=False)

    class Meta:
        model = Account
        fields = ('id', 'number', 'client', 'currencyType', 'currency', 'amount')


class TransferSerializer(serializers.HyperlinkedModelSerializer):
    # accountFrom = serializers.PrimaryKeyRelatedField(many=False, read_only=False)
    # accountTo = serializers.PrimaryKeyRelatedField(many=False, read_only=False)

    class Meta:
        model = Transfer
        fields = ('id', 'accountFrom', 'accountTo', 'amount')
