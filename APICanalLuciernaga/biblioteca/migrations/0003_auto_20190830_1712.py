# Generated by Django 2.2.3 on 2019-08-30 17:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_biblioteca_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biblioteca',
            name='descripcion',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Descripción'),
        ),
    ]