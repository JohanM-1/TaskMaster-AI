# Generated by Django 5.0.12 on 2025-02-25 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('version', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Requerimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('version', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('version', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField()),
                ('version', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='VersionProyect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('proyect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_documents.proyect')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VersionRequerimientos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('requerimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_documents.requerimientos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VersionTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_documents.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VersionUserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.PositiveIntegerField(default=1)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('user_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_documents.userhistory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
