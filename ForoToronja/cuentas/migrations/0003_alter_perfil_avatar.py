# Generated by Django 5.1.6 on 2025-03-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_rename_usuario_perfil_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares/'),
        ),
    ]
