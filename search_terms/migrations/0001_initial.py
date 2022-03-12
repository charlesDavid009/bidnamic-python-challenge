# Generated by Django 4.0.3 on 2022-03-10 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adgroups', '0001_initial'),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search_Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='date')),
                ('clicks', models.IntegerField(verbose_name='clicks')),
                ('cost', models.FloatField(verbose_name='cost')),
                ('conversion_value', models.IntegerField(verbose_name='conversion_value')),
                ('conversions', models.IntegerField(verbose_name='conversion')),
                ('search_term', models.TextField(blank=True, null=True, verbose_name='search_term')),
                ('ad_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adgroups.adgroups')),
                ('campaign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.campaigns')),
            ],
        ),
    ]