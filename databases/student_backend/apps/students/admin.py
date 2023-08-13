from django.contrib import admin

from apps.students.models import Student, University, StudentPass

admin.site.register(Student)
admin.site.register(University)
admin.site.register(StudentPass)
