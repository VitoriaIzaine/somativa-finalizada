# Generated by Django 3.2.9 on 2021-11-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro_medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('especialidade', models.CharField(max_length=30)),
                ('mostrar', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')),
            ],
        ),
    ]
