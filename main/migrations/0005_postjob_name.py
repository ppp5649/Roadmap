# Generated by Django 4.0.1 on 2022-01-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_postjob_datecreate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postjob',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='job'),
        ),
    ]
