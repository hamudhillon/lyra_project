# Generated by Django 3.2.6 on 2022-09-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20220927_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='global_box',
            name='Other_Costs',
            field=models.FloatField(null=True),
        ),
    ]