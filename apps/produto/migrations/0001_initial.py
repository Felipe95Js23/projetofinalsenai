# Generated by Django 4.2.6 on 2023-10-18 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('quantidade', models.BigIntegerField()),
                ('estoque', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='estoque.estoque')),
            ],
        ),
    ]
