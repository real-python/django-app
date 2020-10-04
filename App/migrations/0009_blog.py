# Generated by Django 2.2 on 2020-09-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_userdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('tag', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Blog/')),
            ],
        ),
    ]
