# Generated by Django 5.0.2 on 2024-02-29 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibbitz1', '0011_business_marketing_testimonial_videoblog_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoblog',
            name='logo_admin',
            field=models.FileField(default=2, upload_to='videoblog_admin/'),
            preserve_default=False,
        ),
    ]