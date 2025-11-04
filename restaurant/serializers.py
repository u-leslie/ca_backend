from rest_framework import serializers
from .models import MenuItem, Table, Order, OrderItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        total = 0
        for i in items_data:
            menu = i['menu_item']
            qty = i['quantity']
            if menu.stock < qty:
                raise serializers.ValidationError(f"Not enough stock for {menu.name}")
            OrderItem.objects.create(order=order, **i)
            total += menu.price * qty
            menu.stock -= qty
            menu.save()
        order.total = total
        order.save()
        return order