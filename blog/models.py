from django.db import models


class Post(models.Model):
    author = models.ForeignKey(
        verbose_name='저자',
        to='users.User',
        editable=False,
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(
        verbose_name='제목',
        max_length=255,
    )
    contents = models.TextField(
        verbose_name='내용',
        default='',
    )
    create_at = models.DateTimeField(
        verbose_name='생성일',
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        verbose_name='수정일',
        auto_now=True,
    )

    def __str__(self):
        return '<Blog %s>' % self.id

    class Meta:
        db_table = 'blog'
        verbose_name = '게시글'
        verbose_name_plural = '게시글들'
