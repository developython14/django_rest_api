# Generated by Django 4.1.7 on 2023-04-25 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_alter_story_image_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story_image',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='story.story'),
        ),
    ]
