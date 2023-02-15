# Generated by Django 4.1.3 on 2023-02-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('messages_sent', models.IntegerField(default=0)),
            ],
        ),
    ]
