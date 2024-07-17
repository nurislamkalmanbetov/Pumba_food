# Generated by Django 5.0.6 on 2024-07-16 04:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_slug_food'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_offers', to='product.food')),
            ],
            options={
                'verbose_name': 'Специальное предложение',
                'verbose_name_plural': 'Специальные предложения',
            },
        ),
    ]