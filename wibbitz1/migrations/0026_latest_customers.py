# Generated by Django 5.0.2 on 2024-03-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibbitz1', '0025_alter_img_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Latest_customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media10/')),
            ],
        ),
    ]