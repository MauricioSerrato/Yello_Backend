# Generated by Django 4.1.1 on 2022-09-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]