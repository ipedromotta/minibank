from decimal import Decimal

from django.db import transaction

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import CustomUser


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
            status = 200
        else:
            message = 'Algo deu errado'
            status = 500
    except:
        message = 'Algo deu errado'
        status = 500
    
    return Response({"status": status, "response": message, "accountBalance": user.balance if user else None})

@api_view(['POST'])
def withdraw(request):
    try:
        user = None
        username = request.user
        amount = request.data.get('amount', None)
        if amount and username:
            user = CustomUser.objects.get(username=username)
            if user.balance < Decimal(amount):
                message = 'Saldo insuficiente'
                status = 401
            else:
                user.balance -= abs(Decimal(amount))
                user.save()
                message = 'Saque realizado com sucesso'
                status = 200
        else:
            message = 'Algo deu errado'
            status = 500
    except:
        message = 'Algo deu errado'
        status = 500
                
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

            if user.balance < Decimal(amount):
                message = 'Saldo insuficiente'
                status = 401
            else:
                with transaction.atomic():
                    user.balance -= abs(Decimal(amount))
                    user.save()
                    
                    user_to.balance += abs(Decimal(amount))
                    user_to.save()
                    
                    message = 'Transferencia realizada com sucesso'
                    status = 200
        else:
            message = 'Algo deu errado'
            status = 500
    except:
        message = 'Algo deu errado' if user_to is not None else 'Usuario destino não existe'
        status = 500
    
    return Response({"status": status, "response": message, "accountBalance": user.balance if user else None})
    