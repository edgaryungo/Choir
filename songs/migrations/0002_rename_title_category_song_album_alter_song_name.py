# Generated by Django 4.2 on 2023-04-19 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Title',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.category'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
