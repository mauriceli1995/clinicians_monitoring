# Generated by Django 4.0.2 on 2022-02-18 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_alter_measurement_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='pub_date',
            new_name='submitted_date',
        ),
    ]
