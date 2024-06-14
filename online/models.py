from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):
    '''Student uchun Ustozlar'''
    image = models.ImageField(upload_to='teachers/')
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    experience = models.IntegerField(help_text='tajribasi /yil')
    knowledge = models.CharField(max_length=255, help_text='misol: Python')


    def __str__(self):
        return self.full_name




class Family(models.Model):
    '''Studentlar oilasi'''
    mother_name = models.TextField(help_text='onasini ismi')
    father_name = models.TextField(help_text='otasini ismi')
    familiy_number = models.IntegerField(help_text='oilada nechtasizlar')

    def __str__(self):
        return self.father_name




class Student(models.Model):
    '''Oquvchilar'''
    family = models.OneToOneField(Family, on_delete=models.SET_NULL, null=True)
    teacher = models.ManyToManyField(Teacher)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    image = models.ImageField(upload_to='students/')
    qurilma = models.CharField(max_length=255, help_text='qanday qurilma ishlatishi')
    phone = models.CharField(max_length=13)
    the_border = models.BooleanField(default=False, help_text='chegaraga chiqanmisiz')
    region = models.CharField(max_length=150, help_text='yashash joyi')
    place_of_birth = models.CharField(max_length=150, help_text="tug'ilgan joy")


    def __str__(self):
        return self.full_name






class Topics(models.Model):
    '''Course lar uchun mavzular'''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Course(models.Model):
    '''Oquvchilar uchun kurs'''
    teacher = models.ManyToManyField(Teacher)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    name = models.CharField(max_length=50)
    platform = models.CharField(max_length=150, help_text='qaysi platformada dars bolib otishi')
    opening_time = models.DateTimeField(auto_now_add=True)
    closing_time = models.DateTimeField(null=True, blank=True)
    graduate = models.BooleanField(default=False, help_text='guruh bitirildimi ? ')
    duration = models.DecimalField(max_digits=10,decimal_places=2, help_text='course davomiyligi')
    kunlar = models.CharField(max_length=155, help_text='dars kunlari')


    def __str__(self):
        return self.name



class Comment(models.Model):
    '''Comentariya qoldirish qismi'''
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text='Studentni tanlash')
    title = models.TextField()

    def __str__(self):
        return self.title


class Evaluation(models.Model):
    '''baho qoldirish'''
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    baho = models.BooleanField(help_text='True dars yoqdi manosini bildiradi')


    def __str__(self):
        return self.baho




class TeacherHomework(models.Model):
    '''Uyga vazifa'''
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teacher_homework/', help_text='homework.png')
    video = models.FileField(upload_to='videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'WMW'])
    ], help_text='dars videosi', null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, help_text='uyga vazifa berilgan vaqt')
    time_duration = models.DateTimeField(help_text='uyga vazifa davomiyligi')


    def __str__(self):
        return self.description


class StudentHomework(models.Model):
    '''Studentning uyga vazifasi'''
    teacherhomework = models.ForeignKey(TeacherHomework, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    homework = models.ImageField(upload_to='student_homework/', null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True, help_text='oquvchi uyga vazifa qilgan vaqt')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description



class SendStudentMessage(models.Model):
    '''Oquvchilarga habar yuborish uchun model'''
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class News(models.Model):
    '''Ustoz beradigan Yangiliklar'''
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class StudentShikoyatlar(models.Model):
    '''Ustozlarga shikoyat uchun model'''
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, help_text='shikoyat bermoqchi bolgan ustoz')
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True, help_text='Oquvchi')
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title
