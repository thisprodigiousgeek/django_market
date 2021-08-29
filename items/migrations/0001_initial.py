# Generated by Django 2.2.20 on 2021-08-29 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='商品名')),
                ('description', models.CharField(max_length=1000, verbose_name='本文')),
                ('price', models.IntegerField(verbose_name='価格')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='画像')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('orders', models.ManyToManyField(related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='注文')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='出品者')),
            ],
        ),
    ]