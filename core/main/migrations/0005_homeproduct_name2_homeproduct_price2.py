# Generated by Django 4.0.5 on 2022-06-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_homeproduct_alter_home_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeproduct',
            name='name2',
            field=models.CharField(max_length=50, null=True, verbose_name='HomeProduct name2'),
        ),
        migrations.AddField(
            model_name='homeproduct',
            name='price2',
            field=models.IntegerField(null=True, verbose_name='HomeProduct price2'),
        ),
    ]
