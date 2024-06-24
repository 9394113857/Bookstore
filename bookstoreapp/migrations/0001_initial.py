# Generated by Django 4.1.7 on 2023-09-28 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contactemail', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('msg', models.TextField(max_length=500)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=400)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('store', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='')),
                ('address', models.TextField(max_length=400)),
            ],
            options={
                'db_table': 'merchant',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100)),
                ('rating', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstoreapp.customer')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstoreapp.merchant')),
            ],
            options={
                'db_table': 'feedbacks',
            },
        ),
        migrations.CreateModel(
            name='Bookstore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('cost', models.BigIntegerField()),
                ('year', models.BigIntegerField()),
                ('discount', models.BigIntegerField()),
                ('description', models.TextField(max_length=100)),
                ('categoty', models.CharField(max_length=100)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstoreapp.merchant')),
            ],
            options={
                'db_table': 'book_details',
            },
        ),
        migrations.CreateModel(
            name='Addcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.CharField(max_length=100)),
                ('cart', models.CharField(max_length=100)),
                ('cost', models.BigIntegerField()),
                ('discount', models.BigIntegerField()),
                ('finalcost', models.BigIntegerField()),
                ('status', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstoreapp.bookstore')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstoreapp.customer')),
            ],
            options={
                'db_table': 'order_book',
            },
        ),
    ]