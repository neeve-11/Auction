# Generated by Django 3.1.2 on 2020-11-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20201110_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='picture',
            field=models.ImageField(default='nothing.jpeg', null=True, upload_to='itempic/'),
        ),
    ]