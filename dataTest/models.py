from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=10) # 이름
    address = models.TextField(max_length=50) # 주소
    phone_number = models.CharField(max_length=15) # 번호
    job_position = models.CharField(max_length=10) # 직위
    age = models.IntegerField() # 나이
    dateTimeOfPosting = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["dateTimeOfPosting"]

