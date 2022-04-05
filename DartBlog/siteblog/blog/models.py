from django.db import models
from django.urls import reverse

'''
Category
========
title, slug

Tag
========
title slug

Post
========
title, slug, author, content, created_at, photo, views, category, tags
'''

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.CharField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    slug = models.CharField(max_length=50, verbose_name='Url_slug', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.CharField(max_length=255, verbose_name='Url_post', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.CharField(max_length=100000, blank=True, verbose_name='Контнент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category,verbose_name='Категория', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']



