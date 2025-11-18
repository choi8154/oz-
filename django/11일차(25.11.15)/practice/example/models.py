from django.db import models

class Books(models.Model):
    CATEGORY = [
        ('poetry', '시집'),
        ('novel', '소설'),
        ('deucation', '교육'),
        ('self-help', '자기개발')
    ]
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY)
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f'[{self.get_category_display()}]  {self.title}'
    
    class Meta:
        verbose_name = '도서정보'
        verbose_name_plural = '도서목록'