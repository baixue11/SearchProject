# Generated by Django 3.1 on 2020-09-11 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPromotionBanner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('desc', models.CharField(max_length=256, verbose_name='描述')),
            ],
            options={
                'verbose_name': '商品表',
                'verbose_name_plural': '商品表',
                'db_table': 'product_info',
            },
        ),
    ]