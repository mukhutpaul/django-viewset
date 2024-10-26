# Generated by Django 5.1.2 on 2024-10-26 05:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('description', models.TextField()),
                ('price_range', models.CharField(choices=[('$', 'Very Cheap'), ('$$', 'Cheap'), ('$$$$', 'Moderate'), ('$$$$$', 'Expennsive')], max_length=10)),
                ('street_adress', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('hour', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('ordinal', models.IntegerField()),
                ('business', models.ManyToManyField(to='reviews.business')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('stars', models.IntegerField()),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.business')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
