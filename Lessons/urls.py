# Django
from django.urls import path, include
from .models import Lessons
from Lessons.Apis.api import PostApi,ChangeStatus

# Local

urlpatterns = [
    path("list/", PostApi.as_view(), name="lesson-list"),
    path("change-status/", ChangeStatus.as_view(), name="change-status-lesson"),
    


]
