# Generated by Django 3.2.9 on 2021-12-20 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppURC', '0002_auto_20211215_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='siniestros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSiniestro', models.DateField()),
                ('reclamado', models.BooleanField()),
                ('montoImplicado', models.IntegerField()),
                ('detalle', models.CharField(max_length=140)),
            ],
        ),
    ]