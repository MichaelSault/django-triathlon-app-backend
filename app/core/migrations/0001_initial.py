# Generated by Django 3.2.10 on 2021-12-16 19:22

import core.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=4)),
                ('time_hours', models.IntegerField()),
                ('time_minutes', models.IntegerField()),
                ('time_seconds', models.IntegerField()),
                ('elevation', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sport', models.CharField(choices=[('run', 'Run'), ('bike', 'Bike'), ('swim', 'Swim')], default='run', max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('start_time', models.TimeField(default='12:00')),
                ('title', models.CharField(default='My Workout<function now at 0x7f3583afef70>', max_length=255)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('type', models.CharField(choices=[('cd', 'Cool Down'), ('workout', 'Workout'), ('wu', 'Warm Up'), ('race', 'Race')], default='workout', max_length=255)),
                ('effort', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('image', models.ImageField(null=True, upload_to=core.models.activity_image_file_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
