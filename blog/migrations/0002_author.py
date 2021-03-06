# Generated by Django 3.1.7 on 2021-03-08 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('number', models.IntegerField(null=True, unique=True)),
                ('email', models.CharField(max_length=200, null=True, unique=True)),
                ('company_url', models.CharField(max_length=100, null=True)),
                ('company', models.URLField(null=True)),
                ('date_created', models.DateField(null=True)),
                ('author_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'User Information',
            },
        ),
    ]
