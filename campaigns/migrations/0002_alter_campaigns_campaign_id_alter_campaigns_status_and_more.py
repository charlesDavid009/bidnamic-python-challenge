# Generated by Django 4.0.3 on 2022-03-10 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='campaign_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='status',
            field=models.CharField(max_length=7),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='structure_value',
            field=models.TextField(),
        ),
    ]