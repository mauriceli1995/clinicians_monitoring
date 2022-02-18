# Generated by Django 4.0.2 on 2022-02-18 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('blood_pressure', models.DecimalField(decimal_places=2, max_digits=5)),
                ('body_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
    ]