# Generated by Django 2.2.11 on 2020-04-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_auto_20200330_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='select_contents',
            field=models.ManyToManyField(related_name='select_profiles', to='contents.Contents', verbose_name='찜한 컨텐츠'),
        ),
    ]
