# Generated by Django 2.0 on 2018-01-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180124_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
