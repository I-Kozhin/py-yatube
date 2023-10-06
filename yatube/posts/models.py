from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts" # Вот тут может назвать по другому?
    )
    # отношение между моделями описано через ForeignKey, внтури него мы задаём related_name, значит когда мы обращаемся
    # к объекту класса Group, то  благодаря метаклассам, у него появялеся атрибук, который указан здесь
    # То есть задавая здесь related_name="posts", мы подсказываем программе, что экземпляр класса Group имеет доступ
    # к объектам Post через аттрибут указанный в related_name
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True
    )

    # здесь Group в '', потому что оно объявляется позже, чем образение к нему в Post
    class Meta:
        ordering = ['-pub_date']


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
