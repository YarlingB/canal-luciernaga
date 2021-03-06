# Generated by Django 2.2.3 on 2019-08-27 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('noticias', '0001_initial'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicacion',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comunicacion',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticias.Categoria'),
        ),
        migrations.AddField(
            model_name='comunicacion',
            name='pais',
            field=models.ForeignKey(on_delete=255, to='lugar.Pais'),
        ),
        migrations.AddField(
            model_name='comunicacion',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
