from decimal import Decimal
from datetime import datetime

from django.db import transaction

from rest_framework import status as statusEnum
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import CustomUser, Transactions
from .serializers import TransactionsSerializer


@api_view(['POST'])
def deposit(request):
    try:
        user = None
        username = request.user
        amount = request.data.get('amount', None)
        if amount and username:
            user = CustomUser.objects.get(username=username)
            user.balance += abs(Decimal(amount))
            user.save()
            message = 'Deposito realizado com sucesso'
            status = statusEnum.HTTP_200_OK
            
            Transactions().create_transaction(user, amount, 'deposit')
        else:
            message = 'Algo deu errado'
            status = statusEnum.HTTP_500_INTERNAL_SERVER_ERROR
    except:
        message = 'Algo deu errado'
        status = statusEnum.HTTP_500_INTERNAL_SERVER_ERROR
    
    return Response({"status": status, "response": message, "accountBalance": user.balance if user else None})

@api_view(['POST'])
def withdraw(request):
    try:
        user = None
        username = request.user
        amount = request.data.get('amount', None)
        if amount and username:
            user = CustomUser.objects.get(username=username)
            if user.balance < abs(Decimal(amount)):
                message = 'Saldo insuficiente'
                status = statusEnum.HTTP_401_UNAUTHORIZED
            else:
                user.balance -= abs(Decimal(amount))
                user.save()
                message = 'Saque realizado com sucesso'
                status = statusEnum.HTTP_200_OK
                
                Transactions().create_transaction(user, amount, 'withdraw')
        else:
            message = 'Algo deu errado'
            status = statusEnum.HTTP_500_INTERNAL_SERVER_ERROR
    except:
        message = 'Algo deu errado'
        status = statusEnum.HTTP_500_INTERNAL_SERVER_ERROR
                
    return Response({"status": status, "response": message, "accountBalance": user.balance if user else None})

@api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
def transfer(request):
    try:
        user = None
        user_to = None
        username = request.user
        username_to = request.data.get('username_to', None)
        amount = request.data.get('amount', None)
        
        if username and username_to and amount:
            user = CustomUser.objects.get(username=username)
            user_to = CustomUser.objects.get(username=username_to)

            if user.balance < abs(Decimal(amount)):
                message = 'Saldo insuficiente'
                status = statusEnum.HTTP_401_UNAUTHORIZED
            else:
                with transaction.atomic():
                    user.balance -= abs(Decimal(amount))
                    user.save()
                    
                    user_to.balance += abs(Decimal(amount))
                    user_to.save()
                    
                    Transactions().create_transaction(user, amount, 'transfer')
                    Transactions().create_transaction(user_to, amount, 'deposit')
                    
                    message = 'Transferencia realizada com sucesso'
                    status = statusEnum.HTTP_200_OK
        else:
            message = 'Algo deu errado'
            status = statusEnum.HTTP_500_INTERNAL_SERVER_ERROR
    except:
        message = 'Algo deu errado' if user_to is not None else 'Usuario destino não existe'
        status = statusEnum.HTTP_500_INTERNAL_SERVER_ERROR
    
    return Response({"status": status, "response": message, "accountBalance": user.balance if user else None})
    
@api_view(['POST'])
def get_transactions(request):
    username = request.user
    date = request.data.get('date', datetime.now().strftime('%Y-%m-%d'))
    
    user = CustomUser.objects.get(username=username)
    transactions = Transactions.objects.filter(user=user, created_at__gte=f'{date} 00:00:00', created_at__lte=f'{date} 23:59:59')
    serializer = TransactionsSerializer(transactions, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def alter_user(request):
    try:
        username = request.user
        new_username = request.data.get('username', None)
        new_email = request.data.get('email', None)
        new_name = request.data.get('name', None)
        current_password = request.data.get('current_password', None)
        
        user = CustomUser.objects.get(username=username)
        if username and new_username and new_email and new_name and current_password:
            if user.check_password(current_password):
                user.username = new_username
                user.email = new_email
                user.first_name = new_name
                user.save()
                return Response({"status": statusEnum.HTTP_200_OK, "response": "Usuario alterado com sucesso"})
            else:
                return Response({"status": statusEnum.HTTP_401_UNAUTHORIZED, "response": "Senha incorreta"})
        else:
            return Response({"status": statusEnum.HTTP_500_INTERNAL_SERVER_ERROR, "response": "Algo deu errado"})
        
    except:
        return Response({"status": statusEnum.HTTP_500_INTERNAL_SERVER_ERROR, "response": "Algo deu errado"})
