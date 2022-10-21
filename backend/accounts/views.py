from decimal import Decimal

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
            user.balance += Decimal(amount)
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
                user.balance -= Decimal(amount)
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