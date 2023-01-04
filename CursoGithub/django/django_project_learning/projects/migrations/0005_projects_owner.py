# Generated by Django 3.2.5 on 2023-01-04 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
        ('projects', '0004_projects_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]