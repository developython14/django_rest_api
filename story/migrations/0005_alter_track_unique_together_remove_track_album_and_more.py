# Generated by Django 4.1.7 on 2023-04-27 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_album_track'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='track',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='track',
            name='album',
        ),
        migrations.AlterField(
            model_name='story_image',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.story'),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
    ]