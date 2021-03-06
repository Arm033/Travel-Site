# Generated by Django 4.0.5 on 2022-06-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_product_detail_imgs1_product_detail_imgs2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='media', verbose_name='Blog img1')),
                ('imgw', models.ImageField(upload_to='media', verbose_name='Blog img2')),
                ('name1', models.CharField(max_length=50, verbose_name='Blog name1')),
                ('name2', models.CharField(max_length=50, verbose_name='Blog name2')),
                ('about', models.TextField(verbose_name='Blog about')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
