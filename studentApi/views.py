from rest_framework.decorators import api_view
from rest_framework.response import Response
from studentApi import serializers, models
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    DestroyAPIView
)
import json


# Create your views here.

# To retrive List of students
class StudentList(ListAPIView):
   queryset = models.Student.objects.all()
   serializer_class = serializers.StudentSerializer


# To retrive details of a single student based on pk
class StudentDetail(RetrieveAPIView):
   queryset = models.Student.objects.all()
   serializer_class = serializers.StudentSerializer

# To create students
class CreateStudent(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# To update student details
class UpdateStudent(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# To delete a student record
class DeleteStudent(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer



'''
# @api_view()
# def StudentAPI(request):
#   students = models.Student.objects.all()
#   response = serializers.StudentSerializer(students, many = True)
#   return Response(response.data)

# @api_view(["POST"])
# def createStudentAPI(request):
#   body = json.loads(request.body)
#   response = serializers.StudentSerializer(data = body)
#   if response.is_valid():
#     inst = response.save()
#     response = serializers.StudentSerializer(inst)
#     return Response(response.data)
#   return Response(response.errors)
'''
