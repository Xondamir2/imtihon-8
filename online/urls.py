'''Urls'''
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from .views import TeacherModelView, FamilyModelView, StudentModelView, TopicsModelView, CourseModelView, CommentModelView, EvaluationModelView, TeacherHomeworkModelView, StudentHomeworkModelView, SendStudentMessageAPIView, NewsModelView, StudentShikoyatlarModelView, Filter

'''Default Router Ulanyapti Ishni ossonlashtirish uchun'''
router = DefaultRouter()
router.register('teachers', TeacherModelView)
router.register('family', FamilyModelView)
router.register('students', StudentModelView)
router.register('topics', TopicsModelView)
router.register('courses', CourseModelView)
router.register('comments', CommentModelView)
router.register('evaluations', EvaluationModelView)
router.register('teacher-homework', TeacherHomeworkModelView)
router.register('student-homework', StudentHomeworkModelView)
router.register('news', NewsModelView)
router.register('student-shikoyatlar', StudentShikoyatlarModelView)
'''router ulandi'''


'''Bu yerda swagger ulanmoqda'''
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
'''swagger ulandi'''


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), # swagger uchun ustun
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # swagger uchun ustun
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # swagger uchun ustun
    path('send-message/', SendStudentMessageAPIView.as_view()),
    path('', include(router.urls)), # router uchun ustun
    path('search/', Filter.as_view()), # topics ohtarish uchun
    path('api-auth/', include('rest_framework.urls')),
]