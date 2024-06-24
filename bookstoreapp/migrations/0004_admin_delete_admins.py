# Generated by Django 4.1.7 on 2023-10-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapp', '0003_admins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
        migrations.DeleteModel(
            name='Admins',
        ),
    ]