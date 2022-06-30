# Generated by Django 4.0.5 on 2022-06-27 10:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(choices=[('son', 'son'), ('daughter', 'daughter'), ('brother', 'brother'), ('sister', 'sister'), ('mother', 'mother'), ('father', 'father')], max_length=32)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\221?\\d{9,10}$')])),
                ('email', models.EmailField(blank=True, max_length=64)),
                ('address', models.CharField(blank=True, max_length=32)),
                ('profession', models.CharField(blank=True, max_length=32)),
                ('age', models.IntegerField(blank=True)),
                ('sex', models.CharField(blank=True, max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\221?\\d{9,10}$')])),
                ('address', models.CharField(blank=True, max_length=32)),
                ('profession', models.CharField(blank=True, max_length=32)),
                ('age', models.IntegerField(blank=True)),
                ('sex', models.CharField(blank=True, max_length=8)),
                ('profile', models.BooleanField(default=False)),
                ('relative', models.ManyToManyField(related_name='profiles', to='api.relatives')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
