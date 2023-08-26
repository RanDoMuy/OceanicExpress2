# Generated by Django 4.1.6 on 2023-08-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logincred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('Password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Package_Description', models.CharField(max_length=50, verbose_name='Package Description')),
                ('Quantity', models.IntegerField(verbose_name='Quantity')),
                ('Weight', models.IntegerField(verbose_name='Package Weight')),
                ('Package_Condition', models.CharField(max_length=50, verbose_name='Package Condition')),
                ('Sender_FullName', models.CharField(max_length=50, verbose_name='Sender Fullname')),
                ('Sender_Email', models.EmailField(max_length=20, verbose_name='Sender Email Address')),
                ('Sender_Address', models.CharField(max_length=50, verbose_name='Sender Address')),
                ('Sender_Contact', models.CharField(max_length=11, verbose_name='Sender Contact')),
                ('Receiver_FullName', models.CharField(max_length=50, verbose_name='Receiver Fullname')),
                ('Receiver_Email', models.EmailField(max_length=20, verbose_name='Receiver Email address')),
                ('Receiver_Address', models.CharField(max_length=50, verbose_name='Receiver Address')),
                ('Receiver_Contact', models.CharField(max_length=11, verbose_name='Receiver Contact')),
                ('Shipping_Plan', models.CharField(max_length=50, verbose_name='Shipping Plan')),
                ('Shipment_Status', models.CharField(max_length=50, verbose_name='Shipment Status')),
                ('Shipment_Destination', models.CharField(max_length=50, verbose_name='Shipment Destination')),
                ('Current_Location', models.CharField(max_length=50, verbose_name='Current Package Location')),
                ('Dispatch_Date', models.DateField(verbose_name='Dispatch Date')),
                ('Dispatch_Location', models.CharField(max_length=50, verbose_name='Dispatch Location')),
                ('Expected_Delivery_Date', models.DateField(verbose_name='Expected Delivery Date')),
                ('Tracking_Id', models.CharField(max_length=10, verbose_name='Tracking ID')),
            ],
        ),
        migrations.CreateModel(
            name='signupcred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=50, verbose_name='Fullname')),
                ('Number', models.IntegerField(verbose_name='Phone Number')),
                ('Email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('Password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
    ]
