from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/events/', include('event_reg.urls')),
    path('api/restaurant/', include('restaurant.urls')),
    path('api/jobs/', include('job_board.urls')),
]