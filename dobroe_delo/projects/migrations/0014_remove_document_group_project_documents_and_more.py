# Generated by Django 5.1.5 on 2025-03-14 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_alter_project_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='group',
        ),
        migrations.AddField(
            model_name='project',
            name='documents',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='projects.document', verbose_name='Документы'),
        ),
        migrations.DeleteModel(
            name='DocumentGroup',
        ),
    ]
