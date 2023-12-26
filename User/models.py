# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, send_mail, BaseUserManager

# Local
from User.services.validators import ValidatorPhoneNumber


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Roles(BaseModel):
    title = models.CharField(verbose_name="عنوان",max_length=64)
    is_active = models.BooleanField(verbose_name="فعال", default=True)
    description = models.TextField(verbose_name="توضیحات", blank=True,null=True)
    
    # Created Time
    # Updated Time
    
    class Meta:
        db_table = "Roles"
        verbose_name = _("Role")
        verbose_name_plural = "نقش ها"
        
    def __str__(self):
        return self.title
    


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number,email, password , is_staff, is_superuser, **extra_fields):
        
        now = timezone.now()
        user = self.model(phone_number=phone_number,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          date_joined=now,
                          email=email,
                          **extra_fields)

        if not extra_fields.get('no_password'):
            user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password, **extra_fields):

        is_staff = False
        is_superuser = False
        email = None
        return self._create_user(phone_number,  email,password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, phone_number, email, password, **extra_fields):

        is_staff = True
        is_superuser = True
        return self._create_user(phone_number, email, password, is_staff, is_superuser, **extra_fields)

    def get_by_phone_number(self, phone_number):
        return self.get(**{'phone_number': phone_number})


class BaseUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.BigIntegerField(
        verbose_name='شماره تلفن',
        unique=True,
        validators=[ValidatorPhoneNumber],
        error_messages={
            'unique': _("A user with that phone number already exists."),
        },
        null=True,
    )
    role = models.ForeignKey(Roles,verbose_name="نقش",on_delete=models.PROTECT,null=True)
    # optional
    name = models.CharField(
        _('name'), max_length=64, blank=True, null=True)
    email = models.EmailField(
        verbose_name='ایمیل', unique=True, null=True, blank=True)
    nick_name = models.CharField(verbose_name=_(
        'nick name'), max_length=150, blank=True, null=True)
    avatar = models.ImageField(verbose_name=_(
        'avatar'), upload_to='user/%Y/%m/%d/', blank=True, null=True)
    birthday = models.DateField(verbose_name=_(
        'birthday'), null=True, blank=True)
    gender = models.BooleanField(verbose_name=_('gender'), null=True, blank=True, help_text=_(
        'female is False,male is True,null is unset'))
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'), default=timezone.now)

    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = 'کاربران'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_loggein_user(self):
        return self.phone_number is not None or self.email is not None

    def save(self, *args, **kwargs):
        if self.email is not None and self.email.strip() == '':
            self.email = None
        super().save(*args, **kwargs)

    def __str__(self):
        if self.name:
            return self.name +"-"+ self.role.title
        return str(self.phone_number)
