# Generated by Django 3.1.1 on 2020-10-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('discount', models.IntegerField()),
            ],
        ),
    ]