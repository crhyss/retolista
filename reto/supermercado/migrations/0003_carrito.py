# Generated by Django 3.1.2 on 2020-10-18 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermercado', '0002_producto_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCompra', models.DateField(auto_now=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermercado.producto')),
            ],
        ),
    ]