from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.
class Blog(models.Model):
    CATEGORY = (
    ('read', '독서'),
    ('health', '운동'),
    ('study', '공부'),
    ('hobby', '취미'),
    )
    category = models.CharField('카테고리', max_length=10, choices=CATEGORY)
    title = models.CharField('제목',max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE() => 유저가 삭제되면 같이 삭제
    # models.PROTECT => 블로그가 있으면 유저 삭제 불가
    # models.SET_NULL => 유저 삭제시 블로그의 author가 null이 됨

    created_at = models.DateTimeField('작성일자',auto_now_add=True)
    updated_at = models.DateTimeField('수정일자',auto_now=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title[:10]}"

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'