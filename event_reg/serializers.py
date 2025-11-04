from rest_framework import serializers
from .models import Event, Registration
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source='event.title', read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Registration
        fields = '__all__'