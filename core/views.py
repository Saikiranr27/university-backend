from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# 1️⃣ POST - Save Registration
@api_view(['POST'])
def create_inquiry(request):
    serializer = InquirySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# 2️⃣ GET - Courses
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

# 3️⃣ GET - Faculty + HOD
@api_view(['GET'])
def get_faculty(request):
    faculty = Faculty.objects.all()
    serializer = FacultySerializer(faculty, many=True)
    return Response(serializer.data)

# 4️⃣ GET - Hostel
@api_view(['GET'])
def get_hostel(request):
    hostel = Hostel.objects.all()
    serializer = HostelSerializer(hostel, many=True)
    return Response(serializer.data)

# 5️⃣ GET - Transport
@api_view(['GET'])
def get_transport(request):
    transport = Transport.objects.all()
    serializer = TransportSerializer(transport, many=True)
    return Response(serializer.data)
