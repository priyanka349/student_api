from django.urls import path
from studentApi import views

urlpatterns = [
  path("students/", views.StudentList.as_view()),
  path("students/<int:pk>", views.StudentDetail.as_view()),
  path("createStudent/", views.CreateStudent.as_view()),
  path("updateStudent/<int:pk>", views.UpdateStudent.as_view()),
  path("deleteStudent/<int:pk>", views.DeleteStudent.as_view())
]