from rest_framework import serializers
from .models import Employer, JobListing, Application
from django.contrib.auth.models import User

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

class JobListingSerializer(serializers.ModelSerializer):
    employer_company = serializers.CharField(source='employer.company_name', read_only=True)

    class Meta:
        model = JobListing
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'