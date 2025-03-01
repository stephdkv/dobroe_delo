# Generated by Django 5.1.5 on 2025-01-30 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_document_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название группы')),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название проекта'),
        ),
        migrations.AddField(
            model_name='document',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='projects.documentgroup', verbose_name='Группа'),
        ),
    ]
