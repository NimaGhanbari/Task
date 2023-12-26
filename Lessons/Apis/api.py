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
from Lessons.models import Lessons,Session

User = get_user_model()
#-----------------------------------------------------------------#
# available courses
class SessionSerializer(serializers.ModelSerializer):

        class Meta:
            model = Session
            fields = '__all__'
      
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("phone_number", "role", "name", "email", "avatar", "is_active")


class PostApi(APIView):

    

    class OutPutSerializer(serializers.ModelSerializer):
        teacher = UserSerializer()
        #sessions = SessionSerializer()
        class Meta:
            model = Lessons
            fields = ("title", "teacher", "sessions", "exam_date", "lesson_code", "study_group", "num_units", "is_active")

    

    def get(self, request):
        lessons = Lessons.objects.filter(is_active=True)
        return Response(self.OutPutSerializer(lessons, many=True).data)
# ----------------------------------------------------------------#  
