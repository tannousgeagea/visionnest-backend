# Generated by Django 4.2 on 2024-04-28 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workspace_name', models.CharField(max_length=255)),
                ('workspace_description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Workspace',
                'db_table': 'workspace',
            },
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.CharField(max_length=255)),
                ('image_file', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('annotated', models.BooleanField(default=False)),
                ('annotation', models.FileField(upload_to='labels/')),
                ('processed', models.BooleanField(default=False)),
                ('mode', models.CharField(default='N/A', max_length=255)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.workspace')),
            ],
            options={
                'verbose_name_plural': 'Dataset',
                'db_table': 'dataset',
            },
        ),
    ]
