# Generated by Django 5.0.2 on 2024-02-29 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibbitz1', '0015_alter_marketing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='background',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]