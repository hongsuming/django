from django.db import models

# Create your models here.
class Maker(models.Model):
    m_name = models.CharField(max_length=10)
    m_tel = models.CharField(max_length=30)
    m_addr = models.CharField(max_length=50)
    
    class Meta:
        ordering = ('-id'),
        
    def __str__(self): # 시스템 예약어
        return self.m_name
    
class Product(models.Model):
    p_name = models.CharField(max_length=10)
    p_price = models.IntegerField()
    maker_name = models.ForeignKey(Maker, on_delete=models.CASCADE)  