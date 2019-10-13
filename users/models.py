import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager as _UserManager  # 다른곳에서 User 모델을 부를때 같이 불려와서 귀찮아서 불러오지 않게 설정


class User(AbstractBaseUser):
    """
    처음부터 유저를 구현하기 위해 AbstractBaseUser를 상속받음
    """
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )  # 보안을 위해 uuid를 기본키로 설정
    email = models.EmailField(
        verbose_name='이메일',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name='유저명', 
        max_length=30, 
        unique=True,
    )
    is_active = models.BooleanField(verbose_name='상태', default=True)
    is_admin = models.BooleanField(verbose_name='관리자', default=False, editable=False)

    objects = _UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return '<User %s>' % self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
