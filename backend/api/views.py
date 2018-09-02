from django.contrib.auth.models import User, Group
from .models import Client, CurrencyType, Account, Transfer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from backend.api.serializers import UserSerializer, ClientSerializer,\
    CurrencyTypeSerializer, AccountSerializer, TransferSerializer,\
    GroupSerializer, TokenSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


class CurrencyTypeViewSet(viewsets.ModelViewSet):
    queryset = CurrencyType.objects.all()
    serializer_class = CurrencyTypeSerializer
    # permission_classes = (IsAdminUser,)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = (IsAuthenticated,)


    # Show all of the ACCOUNTS filtering by ID
    def get_account_by_id(self, id):
        queryset = Account.objects.all().filter()
        workspace = self.request.query_params.get('workspace')
        airline = self.request.query_params.get('airline')

        if workspace:
            queryset = queryset.filter(workspace_id=workspace)
        elif airline:
            queryset = queryset.filter(workspace__airline_id=airline)

        return queryset


class TransferViewSet(viewsets.ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    # permission_classes = (IsAuthenticated,)
