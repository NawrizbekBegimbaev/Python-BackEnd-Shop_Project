# Generated by Django 3.2 on 2023-01-25 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип продукта')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('description', models.TextField(default='Description is Empty', max_length=1000, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/', verbose_name='Фото')),
                ('digital', models.BooleanField(default=False, verbose_name='В наличии')),
                ('cart', models.BooleanField(default=False, verbose_name='В карзине')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
