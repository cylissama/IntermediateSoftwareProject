# Generated by Django 4.2.4 on 2023-11-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_submissionattempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztaker',
            name='percentage',
            field=models.DecimalField(decimal_places=0, default=0.0, max_digits=3),
        ),
    ]
