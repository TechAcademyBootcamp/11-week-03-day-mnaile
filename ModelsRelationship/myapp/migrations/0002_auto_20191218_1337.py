# Generated by Django 2.2.8 on 2019-12-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='myapp.Category'),
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
    ]
