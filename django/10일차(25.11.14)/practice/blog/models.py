from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return f'제목 : {self.title}, 생성일자 : {self.created_at}'
    
    class Meta:
        verbose_name = "블로그"
        verbose_name_plural = "블로그 목록"