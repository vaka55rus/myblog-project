# Generated by Django 3.1.2 on 2020-10-17 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201017_1425'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Blogs',
        ),
    ]
