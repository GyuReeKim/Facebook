from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # related_name을 사용하는 이유는 user.post_set이 user과 users에서 중복되기 때문이다.
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")