from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name='分类名称')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    author = models.ForeignKey(User,verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    excerpt = models.CharField(max_length=200,blank=True,verbose_name='摘要')
    body = models.TextField(verbose_name='文章')
    category = models.ForeignKey(Category,verbose_name='分类')
    tag = models.ManyToManyField(Tag,blank=True,verbose_name='标签')
    count = models.PositiveIntegerField(verbose_name='访问次数')

    def get_tags(self):
        return self.tag.all()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ['-modified_time']

    def __str__(self):
        return '{}({})'.format(self.title,self.author.username)



