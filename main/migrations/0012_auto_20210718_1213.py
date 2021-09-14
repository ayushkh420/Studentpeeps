# Generated by Django 3.2.5 on 2021-07-18 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210706_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RequestBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('brandname', models.CharField(default='', max_length=100)),
                ('brandsite', models.CharField(max_length=500)),
                ('want', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
