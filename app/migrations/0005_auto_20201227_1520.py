# Generated by Django 3.1.4 on 2020-12-27 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='expense_type',
            field=models.CharField(choices=[('INC', 'Income'), ('HOU', 'Housing'), ('TRA', 'Transportation'), ('FOO', 'Food & Groceries'), ('UTL', 'Utilities'), ('MED', 'Medical & Insurance'), ('SAV', 'Savings'), ('PER', 'Personal'), ('ENT', 'Entertainment'), ('EDU', 'Education'), ('GIF', 'Gifts & Donations')], default='FOO', max_length=3),
        ),
    ]
