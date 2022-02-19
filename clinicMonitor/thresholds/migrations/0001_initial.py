# Generated by Django 4.0.2 on 2022-02-19 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Threshold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_heart_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_heart_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('min_blood_pressure', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_blood_pressure', models.DecimalField(decimal_places=2, max_digits=5)),
                ('min_body_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_body_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('setting_date', models.DateTimeField(verbose_name='setting date')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
    ]
