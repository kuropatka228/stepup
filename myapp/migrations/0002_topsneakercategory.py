# Generated by Django 5.1.4 on 2025-02-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopSneakerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sneakers', models.ManyToManyField(related_name='categories', to='myapp.sneaker')),
            ],
        ),
    ]
