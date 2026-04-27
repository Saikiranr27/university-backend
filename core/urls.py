from django.urls import path
from .views import *

urlpatterns = [
    path('inquiry/', create_inquiry),
    path('courses/', get_courses),
    path('faculty/', get_faculty),
    path('hostel/', get_hostel),
    path('transport/', get_transport),
]
