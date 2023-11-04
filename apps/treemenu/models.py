from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    title = models.CharField(max_length=220)
    url = models.CharField(max_length=200, unique=True, help_text='Ссылка, например about/ или http://foo.com/')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', 
                               on_delete=models.CASCADE, verbose_name='Родительский пункт')
    active = models.BooleanField("Активность", default=True)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.title
    