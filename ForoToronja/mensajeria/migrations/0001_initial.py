# Generated by Django 5.1.6 on 2025-03-05 04:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('destinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_recibidos', to=settings.AUTH_USER_MODEL)),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes_enviados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
