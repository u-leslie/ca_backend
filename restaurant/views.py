from rest_framework import viewsets, permissions
from .models import MenuItem, Table, Order
from .serializers import MenuItemSerializer, TableSerializer, OrderSerializer

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.IsAdminUser]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('table').prefetch_related('orderitem_set__menu_item')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # optional: lock table
        table = serializer.validated_data['table']
        if table.is_reserved:
            raise serializers.ValidationError("Table already reserved")
        table.is_reserved = True
        table.save()
        serializer.save()