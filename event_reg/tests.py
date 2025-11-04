from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Event, Registration
from datetime import datetime, timedelta

# Test cases for Event Registration API
class EventAPITestCase(APITestCase):
    def setUp(self):
        self.organizer = Usaer.objects.create_user(username='org', password='pass')
        self.user = User.objects.create_user(username='user1', password='pass')
        self.client = APIClient()

        self.event = Event.objects.create(
            title='Django Conference',
            description='Learn Django',
            date=datetime.now() + timedelta(days=10),
            location='Berlin',
            organizer=self.organizer,
        )

    def test_list_events(self):
        response = self.client.get(reverse('event-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_event(self):
        self.client.force_authenticate(user=self.organizer)
        data = {
            'title': 'Python Meetup',
            'description': 'Python talk',
            'date': (datetime.now() + timedelta(days=5)).isoformat(),
            'location': 'Munich',
        }
        response = self.client.post(reverse('event-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_event(self):
        self.client.force_authenticate(user=self.user)
        data = {'event': self.event.id}
        response = self.client.post(reverse('registration-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cancel_registration(self):
        reg = Registration.objects.create(event=self.event, user=self.user)
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('registration-cancel', kwargs={'pk': reg.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        reg.refresh_from_db()
        self.assertTrue(reg.cancelled)