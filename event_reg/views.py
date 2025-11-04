from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related('organizer')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.select_related('event', 'user')
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        reg = self.get_object()
        reg.cancelled = True
        reg.save()
        return Response({'status': 'cancelled'})