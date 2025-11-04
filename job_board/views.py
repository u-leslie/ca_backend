from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import JobListing, Application, Employer
from .serializers import JobListingSerializer, ApplicationSerializer, EmployerSerializer

class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.filter(is_active=True).select_related('employer')
    serializer_class = JobListingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['location', 'employer__company_name']
    search_fields = ['title', 'description']

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.select_related('job', 'applicant')
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)