# Generated by Django 3.2.9 on 2022-01-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_produto_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='codigo',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]
