from rest_framework import serializers
from .models import School, Class, Teacher, StudentsList, Subject


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'SchoolName']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'TeacherName', 'Class', 'Subject']
        depth = 2


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'TeacherName']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'Subject']


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsList
        fields = ['id', 'FirstName', 'LastName']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'ClassName', 'Student']
        depth = 1
