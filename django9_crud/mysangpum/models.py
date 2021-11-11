from django.db import models

# Create your models here.
# 이미 있는 테이블을 가져온 거라 수정하면 안 됨
class Sangdata(models.Model):
    code = models.IntegerField(primary_key=True)
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangdata'