# Generated by Django 5.0.6 on 2024-06-06 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_alter_customuser_cargo_alter_customuser_celular_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='tipo_acesso',
        ),
    ]
