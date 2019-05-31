from django.db import models


class User(models.Model):
    openid = models.CharField(max_length=32, unique=True, verbose_name='用户openid')
    nickname = models.CharField(max_length=100, null=True, blank=True, default='', verbose_name='微信昵称')
    avatar = models.URLField(null=True, blank=True, default='', verbose_name='头像')
    username = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name='真实姓名')
    phone = models.CharField(max_length=11, null=True, blank=True, default='', verbose_name='手机号')
    source_id = models.IntegerField(default=1, verbose_name="用户来源")
    dt_create = models.DateTimeField(auto_now_add=True)
    dt_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'
        ordering = ['-id']

    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, models.ManyToManyField):
                value = [ i.id for i in value ] if self.pk else None
            if isinstance(f, models.DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data
