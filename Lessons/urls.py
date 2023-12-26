# Django
from django.urls import path, include
from .models import Lessons
from Lessons.Apis.api import PostApi

# Local

urlpatterns = [
    path("list/", PostApi.as_view(), name="lesson-list"),
    


]
