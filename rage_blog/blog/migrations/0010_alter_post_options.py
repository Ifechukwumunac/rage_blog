# Generated by Django 4.0.6 on 2022-07-21 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-updated',)},
        ),
    ]
