# Generated by Django 5.0.1 on 2024-03-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_askqa_detail_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askqa',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ชื่อผู้ติดต่อ'),
        ),
    ]
