# Generated by Django 2.0 on 2018-01-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20180125_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='imagem',
            field=models.FileField(upload_to='core/static/img'),
        ),
    ]