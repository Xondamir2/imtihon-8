'''Views'''
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import (Teacher, Family, Student, Topics, Course,
                     Comment, Evaluation, TeacherHomework, StudentHomework,
                     News,StudentShikoyatlar)
from .serializer import (TeacherSerializerClass, FamilySerializerClass, StudentSerializerClass, TopicsSerializerClass,
                         CourseSerializerClass, CommentSerializerClass, EvaluationSerializerClass,
                         TeacherHomeworkSerializerClass, StudentHomeworkSerializerClass, NewsSerializerClass,
                         StudentShikoyatlarSerializerClass, SendStudentMessageSerializerClass)
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser
# Create your views here.



'''Teacher Model View'''
class TeacherModelView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializerClass
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]


'''Family Model View'''
class FamilyModelView(ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializerClass
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

'''Student Model View'''
class StudentModelView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializerClass
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]


'''Topics Model View '''
class TopicsModelView(ModelViewSet):
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializerClass
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]



'''Course Model View'''
class CourseModelView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerClass
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]



'''Comment Model View'''
class CommentModelView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerClass




'''Evaluation Model View'''
class EvaluationModelView(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializerClass



'''Teacher Homework Model View'''
class TeacherHomeworkModelView(ModelViewSet):
    queryset = TeacherHomework.objects.all()
    serializer_class = TeacherHomeworkSerializerClass


'''Student Homework Model View'''
class StudentHomeworkModelView(ModelViewSet):
    queryset = StudentHomework.objects.all()
    serializer_class = StudentHomeworkSerializerClass



'''News Model View'''
class NewsModelView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializerClass


'''Student Shikoyatlar Model View'''
class StudentShikoyatlarModelView(ModelViewSet):
    queryset = StudentShikoyatlar.objects.all()
    serializer_class = StudentShikoyatlarSerializerClass


'''Studentnig email ga habar yuborish'''
class SendStudentMessageAPIView(APIView):
    def get(self, request):
        serializer = SendStudentMessageSerializerClass()
        return Response(serializer.data)

    def post(self, request):
        serializer = SendStudentMessageSerializerClass(data=request.data)
        serializer.is_valid()

        users = User.objects.all()
        for user in users:
            subject = serializer.validated_data.get('name')
            message = f"Assalomu Alaykum  {user.username} {serializer.validated_data.get('text')}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail(subject, message, email_from, recipient_list)

        return Response('success')


'''Filterlash qismi'''
class Filter(APIView):
    def get(self, request: Request):
        search = str(request.query_params.get('search'))
        topics = Topics.objects.filter(name__icontains=search)
        return Response({'topics': TopicsSerializerClass(topics, many=True).data})


