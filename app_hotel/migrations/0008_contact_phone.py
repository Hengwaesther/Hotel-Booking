# Generated by Django 4.1 on 2022-10-11 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hotel', '0007_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='phone', max_length=20),
            preserve_default=False,
        ),
    ]
