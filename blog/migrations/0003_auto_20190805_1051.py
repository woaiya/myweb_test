# Generated by Django 2.2.4 on 2019-08-05 02:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190619_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=150, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='username',
            field=models.CharField(default='test', max_length=20, verbose_name='用户名'),
        ),
    ]
