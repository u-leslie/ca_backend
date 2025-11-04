from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from django.contrib.auth.models import User
from .models import Employer, JobListing, Application
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile


class JobBoardAPITestCase(APITestCase):
    def setUp(self):
        self.employer_user = User.objects.create_user('emp', password='pass')
        self.applicant = User.objects.create_user('app', password='pass')
        self.client = APIClient()

        self.employer = Employer.objects.create(user=self.employer_user, company_name='Acme')
        self.job = JobListing.objects.create(
            employer=self.employer,
            title='Backend Engineer',
            description='Django role',
            location='Remote',
            salary_min=80000,
            salary_max=120000,
        )

    def test_search_jobs(self):
        response = self.client.get(reverse('joblisting-list'), {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_apply_job(self):
        self.client.force_authenticate(user=self.applicant)
        resume = SimpleUploadedFile('resume.pdf', b'file_content', content_type='application/pdf')
        data = {
            'job': self.job.id,
            'cover_letter': 'I love Django!',
            'resume': resume,
        }
        response = self.client.post(reverse('application-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)