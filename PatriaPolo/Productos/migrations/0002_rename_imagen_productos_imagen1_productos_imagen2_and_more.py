# Generated by Django 4.0.5 on 2022-10-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='imagen',
            new_name='imagen1',
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen2',
            field=models.ImageField(null=True, upload_to='Productos'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen3',
            field=models.ImageField(null=True, upload_to='Productos'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen4',
            field=models.ImageField(null=True, upload_to='Productos'),
        ),
    ]