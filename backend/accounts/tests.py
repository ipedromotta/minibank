from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Transactions
from rest_framework.test import APIClient


User = get_user_model()

class CustomUserTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username="joao", password="senha123", balance=100.00)
        self.assertEqual(user.username, "joao")
        self.assertEqual(user.balance, 100.00)


class TransactionsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="maria", password="senha456", balance=50.00)

    def test_transaction_creation(self):
        tx = Transactions.objects.create(user=self.user, amount=25.00, type="deposit")
        self.assertEqual(tx.amount, 25.00)
        self.assertEqual(tx.type, "deposit")
        self.assertEqual(tx.user.username, "maria")

    def test_create_transaction_method(self):
        tx = Transactions()
        tx.create_transaction(user=self.user, amount=10.00, type="withdrawal")
        self.assertEqual(tx.amount, 10.00)
        self.assertEqual(tx.type, "withdrawal")
        self.assertEqual(tx.user, self.user)


class ViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='joao', password='senha123', balance=100)
        self.client.force_authenticate(user=self.user)

    def test_deposit_sucesso(self):
        response = self.client.post('/api/v1/deposit/', {'amount': 50})
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(float(self.user.balance), 150)

    def test_withdraw_saldo_insuficiente(self):
        response = self.client.post('/api/v1/withdraw/', {
            'amount': 200,
            'current_password': 'senha123'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('Saldo insuficiente', response.data['response'])

    def test_transfer_usuario_destino_inexistente(self):
        response = self.client.post('/api/v1/transfer/', {
            'username_to': 'naoexiste',
            'amount': 10,
            'current_password': 'senha123'
        })
        self.assertEqual(response.status_code, 500)
        self.assertIn('Usuario destino não existe', response.data['response'])
