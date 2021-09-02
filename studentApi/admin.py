from django.contrib import admin
from studentApi import models

# Register your models here.

admin.site.register([
  models.Student,
  models.Institute
])
