# Generated by Django 2.0 on 2018-06-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0002_auto_20180606_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagestocard',
            old_name='image_comment',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='weddingcard',
            name='card_image',
        ),
        migrations.AddField(
            model_name='imagestocard',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]