# Generated by Django 3.1.7 on 2021-03-05 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('store', '0004_auto_20210305_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='storepage',
            name='banner_title',
            field=models.CharField(default='Welcome to the store', max_length=200),
        ),
        migrations.AddField(
            model_name='storepage',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AddField(
            model_name='storepage',
            name='intro',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]