# Generated by Django 4.2.4 on 2023-09-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeteria', '0002_usuario_delete_usarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='endereco',
            field=models.TextField(max_length=255),
        ),
    ]
