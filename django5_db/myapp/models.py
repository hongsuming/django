from django.db import models

# Create your models here.
class Article(models.Model): # 테이블을 클래스로 정의
    code = models.CharField(max_length=10) # CharField, textField, DateTimeField, IntegerField...
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    
    