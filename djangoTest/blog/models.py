from django.db import models

class Post(models.Model):
    
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    #created_at = models.DateTimeField()
    # 자동 시간 설정
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    head_image = models.ImageField(upload_to="blog/images/%Y/%m/%d", blank=True)
    
    
    def __str__(self):
        # pk는 post의 id,  id를 title로 출력 
        return f'[{self.pk}]{self.title}'
    
    def get_absolute_url (self):
        return f'/blog/{self.pk}'
    
# Create your models here.
