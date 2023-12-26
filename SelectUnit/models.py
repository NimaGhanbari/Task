from django.db import models
from User.models import BaseModel
from Lessons.models import Lessons
from django.contrib.auth import get_user_model

User = get_user_model()

class SelectUnit(BaseModel):
    title = models.CharField(verbose_name="عنوان",max_length=128)
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name="Student")
    lesson = models.ManyToManyField(Lessons,related_name="lessons")
    is_active = models.BooleanField("فعال", default=True)
    num_unit = models.PositiveIntegerField()
    # uniqu code = id
    # created time
    # Updated time
    
    class Meta:
        db_table = "SelectUnits"
        verbose_name = "انتخاب واحد"
        verbose_name_plural = "انتخاب واحد ها"

    def __str__(self):
        return self.title