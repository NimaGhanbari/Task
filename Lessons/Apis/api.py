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
class ChangeStatus(APIView):
    
    class InPutSerializer(serializers.Serializer):
        is_active = serializers.BooleanField()
        title = serializers.CharField()
    
    def post(self,request):
        serialize = self.InPutSerializer(data=request.data)
        if serialize.is_valid():
            is_active = serialize.validated_data['is_active']
            title = serialize.validated_data['title']
            lesson = get_object_or_404(Lessons,title__icontains=title)
            lesson.is_active = bool(is_active)
            lesson.save()
            messages.success(
                request, "The course status has been changed successfully.")
        else:
            messages.error(
                request, "There was a problem adding the product to the shopping cart")
        
        return Response({"detail":"You used the status change API"})