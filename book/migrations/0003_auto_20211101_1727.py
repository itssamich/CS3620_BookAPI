# Generated by Django 2.2 on 2021-11-01 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20211101_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdata',
            name='bookAuthor',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='bookCategory',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='bookDescription',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='bookTitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]
