# Generated by Django 5.0.2 on 2024-03-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wibbitz1', '0020_rename_heding_footer_decsription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='hed',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
