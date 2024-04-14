from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models


class User(AbstractUser):
    # username 검증 : 영소문자, 숫자, 하이픈(-), 밑줄(_)만 허용
    username_validator = RegexValidator(
        regex='^[a-z0-9_-]{5,20}$',
        message='Username은 5~20자의 영소문자, 숫자, 특수문자(-, _)로만 구성해야 합니다.',
        code='invalid_username'
    )

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        help_text='필수. 영어 소문자, 숫자, 특수문자(-, _)만 사용 가능; 5-20자.',
        validators=[username_validator],
        error_messages={
            'unique': "이미 존재하는 username 입니다.",
        },
    )

    nickname = models.CharField(
        max_length=10,
        unique=True,
        help_text='필수. 4-10자',
        validators=[
            MinLengthValidator(4, message="닉네임은 최소 4자 이상이어야 합니다.")
        ],
        error_messages={
            'unique': "이미 존재하는 닉네임 입니다.",
        }
    )

    date_updated = models.DateTimeField(auto_now=True)

    profile_img = models.ImageField(
        upload_to="images/", blank=True, default="accounts/default_user.png")

    deleted = models.BooleanField(default=False)
