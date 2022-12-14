# Generated by Django 4.0.6 on 2022-08-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='news/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
