# Generated by Django 3.2.3 on 2021-08-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='no message', max_length=600)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]