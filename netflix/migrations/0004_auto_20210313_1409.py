# Generated by Django 3.1.7 on 2021-03-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0003_auto_20210313_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
