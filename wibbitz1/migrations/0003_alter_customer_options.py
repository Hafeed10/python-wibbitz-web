# Generated by Django 5.0.1 on 2024-02-27 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wibbitz1', '0002_alter_customer_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id']},
        ),
    ]