# Generated by Django 4.1.6 on 2023-08-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oceanic_express', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='Receiver_Contact',
            field=models.CharField(max_length=15, verbose_name='Receiver Contact'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Receiver_Email',
            field=models.EmailField(max_length=50, verbose_name='Receiver Email address'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Sender_Contact',
            field=models.CharField(max_length=15, verbose_name='Sender Contact'),
        ),
        migrations.AlterField(
            model_name='package',
            name='Sender_Email',
            field=models.EmailField(max_length=50, verbose_name='Sender Email Address'),
        ),
    ]