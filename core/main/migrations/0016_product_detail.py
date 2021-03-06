# Generated by Django 4.0.5 on 2022-06-20 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_shopproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='media', verbose_name='Product_detail img1')),
                ('img2', models.ImageField(upload_to='media', verbose_name='Product_detail img2')),
                ('img3', models.ImageField(upload_to='media', verbose_name='Product_detail img3')),
                ('name1', models.CharField(max_length=50, verbose_name='Product_detail  name1')),
                ('name2', models.CharField(max_length=50, verbose_name='Product_detail  name2')),
                ('price', models.IntegerField(verbose_name='Product_detail  price')),
            ],
            options={
                'verbose_name': 'Product_detail',
                'verbose_name_plural': 'Product_details',
            },
        ),
    ]
