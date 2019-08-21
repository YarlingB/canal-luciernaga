# Generated by Django 2.2.3 on 2019-08-21 17:54

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lugar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('siglas', models.CharField(help_text='Siglas o nombre corto de la oganización', max_length=200, verbose_name='Siglas')),
                ('logo', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='contrapartes/logos/')),
                ('slug', models.SlugField(editable=False, max_length=200)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lugar.Pais')),
            ],
            options={
                'verbose_name_plural': 'Organizaciones',
                'verbose_name': 'Organización',
            },
        ),
    ]
