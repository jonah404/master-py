# Generated by Django 4.1.3 on 2022-12-28 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(default='null', upload_to='articles', verbose_name='Miniatura')),
                ('public', models.BooleanField(verbose_name='¿Publicado?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado')),
            ],
            options={
                'verbose_name': ('Articulo',),
                'verbose_name_plural': ('Articulos',),
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=110)),
                ('description', models.CharField(max_length=250)),
                ('created_at', models.DateField()),
            ],
            options={
                'verbose_name': ('Categoria',),
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
