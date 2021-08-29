from django.db import models
from django.conf import settings
 
from django.contrib.auth import get_user_model

User = get_user_model()
 
class Item(models.Model):
    name = models.CharField("商品名", max_length=255)
    description = models.CharField("商品説明", max_length=1000)
    price = models.IntegerField("価格")
    image = models.ImageField("画像", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="出品者")
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    orders = models.ManyToManyField(get_user_model(), related_name="orders", verbose_name="注文") 
    
    def __str__(self):
        return f"{self.name[:20]}: {self.price}円"