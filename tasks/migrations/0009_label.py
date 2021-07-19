# Generated by Django 3.2.5 on 2021-07-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20210718_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Имя')),
                ('tasks', models.ManyToManyField(to='tasks.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
