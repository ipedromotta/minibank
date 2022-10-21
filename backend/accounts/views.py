from decimal import Decimal

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import CustomUser


@api_view(['POST'])
def deposit(request):
    try:
        username = request.user
        amount = request.data.get('amount', None)
        if amount and username:
            user = CustomUser.objects.filter(username=username)
            for attributes in user:
                attributes.balance += Decimal(amount)
                attributes.save()
                message = 'Deposito realizado com sucesso'
                status = 200
        else:
            message = 'Algo deu errado'
            status = 500
            attributes = None
    except:
        message = 'Algo deu errado'
        status = 500
        attributes = None
    
    return Response({"status": status, "response": message, "accountBalance": attributes.balance if attributes else None})

@api_view(['POST'])
def withdraw(request):
    try:
        username = request.user
        amount = request.data.get('amount', None)
        if amount and username:
            user = CustomUser.objects.filter(username=username)
            for attributes in user:
                if attributes.balance < Decimal(amount):
                    message = 'Saldo insuficiente'
                    status = 401
                else:
                    attributes.balance -= Decimal(amount)
                    attributes.save()
                    message = 'Saque realizado com sucesso'
                    status = 200
        else:
            message = 'Algo deu errado'
            status = 500
            attributes = None
    except:
        message = 'Algo deu errado'
        status = 500
        attributes = None
                
    return Response({"status": status, "response": message, "accountBalance": attributes.balance if attributes else None})