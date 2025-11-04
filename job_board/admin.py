from django.contrib import admin
from .models import Employer, JobListing, Application


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user')
    search_fields = ('company_name', 'user__username')


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'is_active', 'posted_at')
    list_filter = ('is_active', 'location')
    search_fields = ('title', 'description')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'status', 'applied_at')
    list_filter = ('status',)
    search_fields = ('job__title', 'applicant__username')
    readonly_fields = ('applied_at',)