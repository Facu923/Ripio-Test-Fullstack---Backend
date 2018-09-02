from django.contrib.auth.models import User, Group
from .models import Client, CurrencyType, Account, Transfer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from backend.api.serializers import UserSerializer, ClientSerializer,\
    CurrencyTypeSerializer, AccountSerializer, TransferSerializer,\
    GroupSerializer, TokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = (TokenAuthentication,)


class CurrencyTypeViewSet(viewsets.ModelViewSet):
    queryset = CurrencyType.objects.all()
    serializer_class = CurrencyTypeSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
