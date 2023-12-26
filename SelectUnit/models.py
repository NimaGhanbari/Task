from django.db import models
from User.models import BaseModel
from Lessons.models import Lessons
from django.contrib.auth import get_user_model

User = get_user_model()


class SelectUnit(BaseModel):
    title = models.CharField(verbose_name="عنوان", max_length=128,blank=True,null=True)
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Student",verbose_name="دانش آموز")
    lesson = models.ManyToManyField(Lessons, related_name="lessons")
    is_active = models.BooleanField("فعال", default=True)
    # uniqu code = id
    # created time
    # Updated time

    @property
    def num_unit(self):
        temp1 = 0
        temp = self.lesson.all()
        for x in temp:
            temp1 += x.num_units
        return temp1

    class Meta:
        db_table = "SelectUnits"
        verbose_name = "انتخاب واحد"
        verbose_name_plural = "انتخاب واحد ها"

    def __str__(self):
        return str(self.title)
