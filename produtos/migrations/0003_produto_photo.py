# Generated by Django 3.2.9 on 2022-01-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_produto_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='produtos_photos'),
        ),
    ]