# Generated by Django 3.1.5 on 2021-02-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20210205_0123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='result',
            new_name='title',
        ),
        migrations.AddField(
            model_name='result',
            name='explain',
            field=models.CharField(max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]