# Generated by Django 2.0.9 on 2018-10-31 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_auto_20181026_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='image',
            field=models.ImageField(default=1, upload_to='notes-img'),
            preserve_default=False,
        ),
    ]