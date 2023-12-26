# Django
from django.urls import path, include
from .models import Lessons
from Lessons.Apis.api import PostApi,ChangeStatus

# Local

urlpatterns = [
    # برای مشاهده لیست دروس ارائه شده
    path("list/", PostApi.as_view(), name="lesson-list"),
    # برای تغییر وضعیت درس
    path("change-status/<int:lesson_id>/", ChangeStatus.as_view(), name="change-status-lesson"),
    


]
