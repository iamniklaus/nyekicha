# Generated by Django 4.1.3 on 2022-12-04 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sacco', '0002_rename_name_sacco_official_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='driver_name',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sacco.sacco_member'),
        ),
        migrations.AlterField(
            model_name='sacco_official',
            name='first_name',
            field=models.CharField(max_length=200, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='sacco_official',
            name='second_name',
            field=models.CharField(max_length=200, null=True, verbose_name='Second Name'),
        ),
    ]
