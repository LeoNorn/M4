# Generated by Django 4.2.6 on 2023-10-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0004_sulpakproducts_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaberlicProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=200)),
                ('title_url', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='SulpakProducts',
        ),
    ]
