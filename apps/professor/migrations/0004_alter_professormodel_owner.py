# Generated by Django 5.1.2 on 2025-05-21 12:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0003_alter_professormodel_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='professormodel',
            name='owner',
            field=models.OneToOneField(limit_choices_to={'is_staff': False, 'is_teacher': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
