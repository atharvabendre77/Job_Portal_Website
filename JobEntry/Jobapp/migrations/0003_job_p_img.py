# Generated by Django 5.0.2 on 2024-03-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0002_job_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='p_img',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]