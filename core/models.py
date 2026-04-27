from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    is_hod = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Hostel(models.Model):
    room_type = models.CharField(max_length=50)
    total_rooms = models.IntegerField()
    available_rooms = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Transport(models.Model):
    route_name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=20)
    total_seats = models.IntegerField()
    available_seats = models.IntegerField()

class Inquiry(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    consent = models.BooleanField()
