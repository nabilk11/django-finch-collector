# Generated by Django 4.0.3 on 2022-03-26 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=500)),
                ('height', models.IntegerField()),
                ('position', models.CharField(choices=[('F', 'Forward'), ('G', 'Guard'), ('C', 'Center')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
