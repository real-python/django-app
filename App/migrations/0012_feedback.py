# Generated by Django 2.2 on 2020-10-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20200920_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
