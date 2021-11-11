from django.db import models

# Create your models here.
class Guest(models.Model):
    # guest_no = models.AutoField(auto_created=True, primary_key=True) # 이렇게 하면 자동으로 만들어지는 id가 없음 (수동적으로 직접 만든 것)
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    class Meta:
        ordering = ('title',)
        ordering = ('-id',)