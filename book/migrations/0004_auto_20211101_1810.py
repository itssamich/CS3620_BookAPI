# Generated by Django 2.2 on 2021-11-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20211101_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdata',
            name='bookImage',
            field=models.ImageField(default='images/none/noimg.jpg', upload_to='images'),
        ),
    ]
