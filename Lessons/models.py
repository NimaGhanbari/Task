from django.db import models
from User.models import BaseModel
from django.contrib.auth import get_user_model

User = get_user_model()


class College(BaseModel):
    title = models.CharField(verbose_name="دانشکده", max_length=64)
    description = models.TextField(verbose_name="توضیحات",blank=True,null=True)
    is_active = models.BooleanField("فعال", default=True)
    class Meta:
        db_table = "College"
        verbose_name = "دانشکده"
        verbose_name_plural = "دانشکده ها"

    def __str__(self):
        return self.title



class Location(BaseModel):
    college = models.ForeignKey(
        College, verbose_name="دانشکده", related_name="colleges", on_delete=models.CASCADE)
    num_class = models.PositiveIntegerField(verbose_name="شماره کلاس")
    is_active = models.BooleanField("فعال", default=True)

    class Meta:
        db_table = "Locations"
        verbose_name = " مکان "
        verbose_name_plural = "مکان ها"

    def __str__(self):
        
        return str(self.college) + " - کلاس " + str(self.num_class)


class Session(BaseModel):
    
    WEEKDAY_CHOICES = (
        ("SATURDAY", 'شنبه'),
        ("SUNDAY", 'یکشنبه'),
        ("MONDAY", 'دوشنبه'),
        ("TUESDAY", 'سه شنبه'),
        ("WEDNESDAY", 'چهارشنبه'),
        ("THURSDAY", 'پنج شنبه'),
        ("FRIDAY", 'جمعه'),
    )
    location = models.ForeignKey(Location, verbose_name="مکان برگزاری", related_name="locations",on_delete=models.CASCADE)
    presentation_time = models.TimeField(verbose_name="زمان برگزاری")
    weekday = models.CharField(choices=WEEKDAY_CHOICES,max_length=15)
    class Meta:
        db_table = "Sessions"
        verbose_name = "جلسه"
        verbose_name_plural = "جلسات"

    def __str__(self):
        return "مکان:" + str(self.location) +"  ساعت:  "+ str(self.presentation_time)
    
    
class Lessons(BaseModel):
    title = models.CharField(verbose_name="عنوان", max_length=128)
    teacher = models.ForeignKey(
        User, verbose_name="معلم", on_delete=models.CASCADE, related_name="Teacher")
    #  به جای دو تا فیلد زیر باید از سشن استفاده کنیم و باید فارنکی باشد
    sessions = models.ManyToManyField(Session,verbose_name="جلسات",related_name="sessions")
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
