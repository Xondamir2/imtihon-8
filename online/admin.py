from django.contrib import admin
from .models import (Teacher, Family, Student, Topics, Course,
                     Comment, Evaluation, TeacherHomework, StudentHomework,
                     News,StudentShikoyatlar,SendStudentMessage)
# Register your models here.


admin.site.register(Teacher)
admin.site.register(Family)
admin.site.register(Student)
admin.site.register(Topics)
admin.site.register(Course)
admin.site.register(Comment)
admin.site.register(Evaluation)
admin.site.register(TeacherHomework)
admin.site.register(StudentHomework)
admin.site.register(News)
admin.site.register(StudentShikoyatlar)
admin.site.register(SendStudentMessage)
