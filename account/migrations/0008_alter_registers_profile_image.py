# Generated by Django 3.2.5 on 2021-07-20 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_unverified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registers',
            name='profile_image',
            field=models.ImageField(default='', upload_to='profile'),
        ),
    ]
