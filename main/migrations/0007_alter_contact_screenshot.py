# Generated by Django 4.2.3 on 2023-07-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_contact_screenshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='screenshots'),
        ),
    ]
