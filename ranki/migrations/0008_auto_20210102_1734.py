# Generated by Django 3.1.4 on 2021-01-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranki', '0007_auto_20210102_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='epetitions',
        ),
        migrations.AddField(
            model_name='card',
            name='repetitions',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='card',
            name='easiness',
            field=models.FloatField(default=2.5),
        ),
        migrations.AlterField(
            model_name='card',
            name='interval',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='card',
            name='quality',
            field=models.IntegerField(default=1),
        ),
    ]
