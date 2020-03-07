from accounts.models import CustomUser
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Journal(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    category = models.ForeignKey(Category, verbose_name='カテゴリー', on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, verbose_name='タグ', blank=True)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    picture1 = models.ImageField(verbose_name='写真①', blank=True, null=True)
    picture2 = models.ImageField(verbose_name='写真②', blank=True, null=True)
    picture3 = models.ImageField(verbose_name='写真③', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Journal'

    def __str__(self):
        return self.title





