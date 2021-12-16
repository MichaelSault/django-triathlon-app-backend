# Generated by Django 3.2.10 on 2021-12-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_activity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('cd', 'Cool Down'), ('race', 'Race'), ('wu', 'Warm Up'), ('workout', 'Workout')], default='workout', max_length=255),
        ),
    ]
