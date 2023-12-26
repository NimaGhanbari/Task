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
from SelectUnit.models import SelectUnit

# Python
import json


User = get_user_model()

# --------------------------------------------------------------#


class SelectUnitApi(APIView):
    
    
    class InPutSerializer(serializers.ModelSerializer):
        lesson_id = serializers.CharField()
        user_id = serializers.CharField()
        
    # This function is for choosing a unit from the courses provided.
    def post(self,request):
        serialize = self.InPutSerializer(data=request.data,many=True, context={"request": request})
        if serialize.is_valid():
            pk = serialize.initial_data["lesson_id"]
            user = get_object_or_404(User,id=serialize.initial_data["user_id"])
            lessons = None
            try:
                lessons = Lessons.objects.get(id=pk)
            except Lessons.DoesNotExist as ex:
                return Response({"detail": f"ERROR: {ex}"})
            ins1 = SelectUnit.objects.filter(student=user,is_active=True)
            if ins1:
                for x in ins1:
                    x.lesson.add(lessons)
                return Response({"detail":"successfully"})
            ins = SelectUnit.objects.create(student=user)
            ins.lesson.set([lessons])
            messages.success(
                    request, "successfully.")
        else:
            messages.error(
                request, "error")
        
        return Response({"detail":"You used API unit selection"})
    
    # This function is used to delete selected units
    def delete(self,request,lesson_id,user_id):
        user = get_object_or_404(User,id=user_id)
        select = get_object_or_404(SelectUnit,student=user,is_active = True)
        lessons = Lessons.objects.get(id=lesson_id)
        select.lesson.remove(lessons)
        messages.success(
                    request, "successfully.")
        return Response({"detail":"You used API Delete unit"})

# ----------------------------------------------#


class StudentLesson(APIView):
    
    # This function is for viewing the students of a course in the order of unit selection time
    def get(self,request,lesson_id):
        lesson = get_object_or_404(Lessons,id=lesson_id)
        selectlist = SelectUnit.objects.filter(lesson=lesson,is_active=True).order_by("created_at")
        userlist = []
        userlist1 = []
        for x in selectlist:
            userlist.append(x.student)
        for x in userlist:
            userlist1.append(x.phone_number)
        return Response(data=json.dumps(userlist1, ensure_ascii=False), status=status.HTTP_200_OK)   
    
# ------------------------------------------------------------------#