# Generated by Django 5.0.2 on 2024-02-29 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibbitz1', '0014_testimonial_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketing',
            name='image',
            field=models.FileField(upload_to='markating/'),
        ),
    ]
