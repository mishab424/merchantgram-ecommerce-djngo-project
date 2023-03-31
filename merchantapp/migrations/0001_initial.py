# Generated by Django 4.1.7 on 2023-03-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admn', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Costomer',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('adress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('costomer_username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('qry', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Merchants',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('merchantid', models.AutoField(primary_key=True, serialize=False)),
                ('adress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('merchant_username', models.CharField(blank=True, max_length=50, null=True)),
                ('costomer_name', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('qty', models.IntegerField()),
                ('costomer_username', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.BooleanField(default=False, null=True)),
                ('total_amount', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('Delivery_place', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('merchant_username', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
        ),
    ]