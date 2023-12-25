from django.db import models
from User.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class College(BaseModel):
    title = models.CharField(verbose_name="دانشکده", max_length=64)
    description = models.TextField(verbose_name="توضیحات")
    is_active = models.BooleanField("فعال", default=True)
    # created time
    # updated time

    class Meta:
        db_table = "College"
        verbose_name = "دانشکده"

    def __str__(self):
        return self.title


class Location(BaseModel):
    college = models.ForeignKey(
        College, verbose_name="دانشکده", related_name="collegs", on_delete=models.CASCADE)
    num_class = models.PositiveIntegerField(verbose_name="شماره کلاس")
    is_active = models.BooleanField("فعال", default=True)

    class Meta:
        db_table = "Locations"
        verbose_name = "مکان"

    def __str__(self):
        names = [f"{self.college}", f"{self.num_class}"]
        return "-".join(names)


# نام ساختمان
# شماره کلاس
# تاریخ ثبت
# تاریخ بروزرسانی

class Lessons(BaseModel):
    title = models.CharField(verbose_name="عنوان", max_length=128)
    teacher = models.ForeignKey(
        User, verbose_name="معلم", on_delete=models.CASCADE, related_name="Users")
    presentation_time = models.DateTimeField()
    location = models.ManyToManyField(
        Location, verbose_name="مکان برگزاری", related_name="locations")
    exam_date = models.DateTimeField(verbose_name="تاریخ امتحان")
    lesson_code = models.PositiveIntegerField()
    study_group = models.PositiveIntegerField()
    num_units = models.PositiveSmallIntegerField()
    is_active = models.BooleanField("فعال", default=True)

    class Meta:
        db_table = "Lessons"
        verbose_name = "درس"
        verbose_name_plural = "دروس"

    def __str__(self):
        return self.title
