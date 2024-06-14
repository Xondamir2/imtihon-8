'''Serializerlar'''

from rest_framework import serializers
from .models import (Teacher, Family, Student, Topics, Course,
                     Comment, Evaluation, TeacherHomework, StudentHomework,
                     News,StudentShikoyatlar,SendStudentMessage)


'''Teacher Serializer'''
class TeacherSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'



'''Family Serializer'''
class FamilySerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


'''Student Serializer'''
class StudentSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



'''Topics Serializer'''
class TopicsSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = '__all__'



'''Course Serializer'''
class CourseSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



'''Comment Serializer'''
class CommentSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



'''Evaluation Serializer'''
class EvaluationSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'




'''Teacher Homework Serializer'''
class TeacherHomeworkSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = TeacherHomework
        fields = '__all__'




'''Student Homework Serializer'''
class StudentHomeworkSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = StudentHomework
        fields = '__all__'




'''News Serializer'''
class NewsSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'




'''Student Shikoyatlar Serializer'''
class StudentShikoyatlarSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = StudentShikoyatlar
        fields = '__all__'




'''Send Student Message Serializer'''
class SendStudentMessageSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = SendStudentMessage
        fields = '__all__'