from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson/',include("Lessons.urls")),
    path('select-unit/',include("SelectUnit.urls")),
    
]
