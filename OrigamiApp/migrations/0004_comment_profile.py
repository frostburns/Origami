# Generated by Django 3.1.4 on 2021-01-16 05:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('OrigamiApp', '0003_auto_20210115_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OrigamiApp.userprofile'),
            preserve_default=False,
        ),
    ]
