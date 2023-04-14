# Generated by Django 4.1.7 on 2023-04-13 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0015_eventbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventbooking',
            name='amount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eventbooking',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventbooking',
            name='feedback',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eventbooking',
            name='reason',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
