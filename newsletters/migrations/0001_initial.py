# Generated by Django 5.1.1 on 2024-11-08 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('created', 'Создана'), ('launched', 'Запущена'), ('completed', 'Завершена')], default='created', max_length=20)),
                ('clients', models.ManyToManyField(to='newsletters.client')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletters.message')),
            ],
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('success', 'Успешно'), ('failed', 'Не успешно')], max_length=20)),
                ('server_response', models.TextField()),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletters.mailing')),
            ],
        ),
    ]
