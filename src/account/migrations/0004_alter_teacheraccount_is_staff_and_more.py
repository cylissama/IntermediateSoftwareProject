# Generated by Django 4.2.4 on 2023-09-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_teacheraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacheraccount',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='teacheraccount',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
