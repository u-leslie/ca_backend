from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import MenuItem, Table, Order, OrderItem


class RestaurantAPITestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin', 'admin@test.com', 'pass')
        self.client = APIClient()

        self.item = MenuItem.objects.create(name='Pizza', price=12.99, stock=10)
        self.table = Table.objects.create(number=1, seats=4)

    def test_menu_list(self):
        response = self.client.get(reverse('menuitem-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        self.client.force_authenticate(user=self.admin)
        data = {
            'table': self.table.id,
            'orderitem_set': [
                {'menu_item': self.item.id, 'quantity': 2}
            ]
        }
        response = self.client.post(reverse('order-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.item.refresh_from_db()
        self.assertEqual(self.item.stock, 8)