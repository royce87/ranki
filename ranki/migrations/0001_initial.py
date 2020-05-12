# Generated by Django 2.1.7 on 2020-05-11 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=160)),
                ('repeat_date', models.DateField(auto_now_add=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('description', models.CharField(blank=True, max_length=160)),
                ('author', models.CharField(max_length=160)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ranki.Deck'),
        ),
    ]