from djongo import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

avatar_path = 'http://localhost:8000/media/'


class UserProfile(AbstractUser):
    gender_choices = (
        ('male', '男'),
        ('female', '女'),
    )
    phone = models.CharField('手机号', max_length=11, blank=True, null=True)
    nick_name = models.CharField('昵称', max_length=50, default='')
    gender = models.CharField('性别', max_length=10, choices=gender_choices, default='female')
    avatar = models.ImageField(upload_to='avatar', default='avatar/avatar.jpg', verbose_name='头像')

    def __str__(self):
        return self.username

    def get_avatar_path(self):
        return avatar_path + str(self.avatar)

    class Meta(AbstractUser.Meta):
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']
