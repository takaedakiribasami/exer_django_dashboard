from django.db import models
from django.core.validators import RegexValidator


class Person(models.Model):
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (3, 'その他'),
    )

    BLOOD_TYPE_CHOICES = (
        (1, 'A型'),
        (2, 'B型'),
        (3, 'O型'),
        (4, 'AB型'),
    )

    name = models.CharField(verbose_name="名前", max_length=100)
    furigana = models.CharField(verbose_name="名前（フリガナ）", max_length=100)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message=(
        "Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    tel_number = models.CharField(
        verbose_name='電話番号', max_length=15, validators=[tel_number_regex], unique=True, null=True)
    email = models.EmailField(verbose_name='メールアドレス',
                              max_length=255, null=True)
    gender = models.IntegerField(
        verbose_name='性別', choices=GENDER_CHOICES, blank=True, null=True)
    blood_type = models.IntegerField(
        verbose_name='血液型', choices=BLOOD_TYPE_CHOICES, blank=True, null=True)
    birthday = models.DateField(verbose_name='誕生日', blank=True, null=True)
    belong = models.CharField(verbose_name="所属", max_length=100)

    class Meta:
        verbose_name_plural = "Person"

    def __str__(self):
        return self.name
