# Generated by Django 3.1.4 on 2020-12-20 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddConstraint(
            model_name='budget',
            constraint=models.UniqueConstraint(fields=('user', 'year', 'month'), name='unique_monthly_budget'),
        ),
    ]