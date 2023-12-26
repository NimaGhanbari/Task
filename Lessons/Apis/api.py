# Django
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages


# REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

# Local
from Lessons.models import Lessons,Session,Location,College
from Lessons.serializer import LessonsSerializer

User = get_user_model()
#-----------------------------------------------------------------#
# available courses -> get

class PostApi(APIView):

    # برای مشاهده دروس ارائه شده
    def get(self, request):
        lessons = Lessons.objects.filter(is_active=True)
        return Response(LessonsSerializer(lessons, many=True).data)
    
    
    
# ----------------------------------------------------------------#  
class ChangeStatus(APIView):
    # برای تغییر وضعیت یک درس
    def put(self,request,lesson_id):
        
        lesson = get_object_or_404(Lessons,id=lesson_id)
        lesson.is_active = not lesson.is_active
        lesson.save()
        messages.success(
            request, "Lesson status changed successfully")
        return Response({"detail":"You used the status change API"})
      
#---------------------------------------------------------------------#
