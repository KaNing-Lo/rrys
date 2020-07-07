from django.db import models

# Create your models here.
class movie(models.Model):
    title=models.CharField('名字', max_length=255)
    level=models.CharField('等级', max_length=255)
    url=models.CharField('链接', max_length=255)
    dramaType=models.CharField('剧种', max_length=255)
    score=models.CharField('评分', max_length=255)
    formerName=models.CharField('原名', max_length=255)
    region=models.CharField('地区', max_length=255)
    language=models.CharField('语言', max_length=255)
    premiereDate=models.CharField('首播', max_length=255)
    company=models.CharField('公司', max_length=255)
    type=models.CharField('类型', max_length=255)
    screenwriter=models.CharField('编剧', max_length=255)
    directors=models.CharField('导演', max_length=255)
    actors=models.CharField('演员', max_length=255)
    imgurl=models.CharField('图片链接', max_length=255)