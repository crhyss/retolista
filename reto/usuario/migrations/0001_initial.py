# Generated by Django 3.1.2 on 2020-10-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.PositiveIntegerField()),
                ('fecha_nacimiento', models.DateTimeField()),
                ('genero', models.CharField(max_length=30)),
            ],
        ),
    ]
