from django.contrib import admin
from .models import School, Class, Teacher, Subject,StudentsList


admin.site.register(School)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(StudentsList)
