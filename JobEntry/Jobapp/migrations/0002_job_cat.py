# Generated by Django 5.0.2 on 2024-02-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Human Resource'), (2, 'Business Development'), (3, 'Marketing')], default=0, verbose_name='Category'),
            preserve_default=False,
        ),
    ]
