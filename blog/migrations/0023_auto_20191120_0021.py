# Generated by Django 2.2.6 on 2019-11-19 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20191119_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='Новина'),
        ),
    ]
