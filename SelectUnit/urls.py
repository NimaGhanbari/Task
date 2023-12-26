# Django
from django.urls import path, include
from SelectUnit.Apis.api import SelectUnitApi,StudentLesson

# Local

urlpatterns = [
    # برای انتخاب واحد
    path("", SelectUnitApi.as_view()),
    # برای مشاهده دانشجویان یک درس بر اساس زمان انتخاب واحد
    path("<int:lesson_id>/", StudentLesson.as_view()),
    # برای حذف واحد های انتخاب شده
    path("<int:lesson_id>/<int:user_id>/", SelectUnitApi.as_view()),
    
    


]
