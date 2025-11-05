from django.db import models


class Blog(models.Model):
    CATEGORY = (
        ('free', '자유'),
        ('travel', '여행'),
        ('cat', '고양이'),
        ('dog', '강아지')
    )

    title = models.CharField('제목', max_length=50)
    category = models.CharField('카테고리', max_length=100, choices=CATEGORY)
    content = models.TextField('본문')

    create_at = models.DateTimeField('작성일지',auto_now_add=True)
    update_at = models.DateTimeField('수정일지', auto_now=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title[:10]}"

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'

# 제목
# 본문
# 작성자
# 작성일자
# 수정일자
# 카테고리

# 썸네일이미지
# 테그