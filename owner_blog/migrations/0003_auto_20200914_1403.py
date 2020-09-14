# Generated by Django 3.1.1 on 2020-09-14 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('owner_blog', '0002_auto_20200914_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerblog',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_profile', to='profiles.userprofile'),
        ),
    ]
