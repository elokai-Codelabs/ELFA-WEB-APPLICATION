# Generated by Django 4.1.3 on 2023-02-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_blog_title_alter_event_event_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
