from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # 'PUBLISH' PODE SER ALTERADO PARA MEU NOME!!!
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # '__STR__' É O TÍTULO DO POST, ALTERÁ-LO!!!
    def __str__(self):
        return self.title