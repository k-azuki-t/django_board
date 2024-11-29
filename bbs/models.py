from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)  ##フィールドオプションon_deleteは、関連先のオブジェクトが削除された際にそのオブジェクト自身がとる挙動を指定
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    ## 汎用ビューでは、データの保存後にget_absolute_urlが呼び出されるようになっている（汎用ビューの種類）
    def get_absolute_url(self):

        ## urlpatternsでname='〇〇'と指定したURLを呼び出す関数
        return reverse('bbs:detail', kwargs={'pk' : self.pk})