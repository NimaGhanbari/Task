

from rest_framework import serializers
from Lessons.models import Lessons,Session,Location,College
from django.contrib.auth import get_user_model

User = get_user_model()

class CollegeSerializer(serializers.ModelSerializer):

        class Meta:
            model = College
            fields = ("title")

class LocationSerializer(serializers.ModelSerializer):
        college = CollegeSerializer(many=True)
        class Meta:
            model = Location
            fields = ("college","num_class")

class SessionSerializer(serializers.ModelSerializer):
        location = LocationSerializer(many=True)
        weekday = serializers.SerializerMethodField()
        class Meta:
            model = Session
            fields = ("location","presentation_time","weekday")
     
      
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("phone_number", "role", "name", "email", "avatar", "is_active")
        
        
class LessonsSerializer(serializers.ModelSerializer):
        teacher = UserSerializer()
        #sessions = SessionSerializer(many=True)
        class Meta:
            model = Lessons
            fields = ("title", "teacher", "sessions", "exam_date", "lesson_code", "study_group", "num_units", "is_active")
