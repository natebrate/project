# Generated by Django 3.1.7 on 2021-03-05 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210305_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storepage',
            old_name='BannerImage',
            new_name='Banner_image',
        ),
        migrations.RenameField(
            model_name='storepage',
            old_name='bannerTitle',
            new_name='banner_title',
        ),
    ]