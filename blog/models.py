from django.db import models
from django.utils import timezone

#class - 객체 정의, post - 모델의 이름, models.Model -  Post가 장고 모델임을 의미합니다. 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 된다고 알게 됩니다.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
                    default=timezone.now)
    published_date = models.DateTimeField(
                    blank=True, null=True)

    #def(함수, 메서드)라는 뜻, publish라는 메서드(method) 입니다.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
