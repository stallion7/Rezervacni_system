# Generated by Django 4.0.4 on 2023-01-11 14:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('slipka_gym', '0003_alter_trenink_misto'),
    ]

    operations = [
        migrations.AddField(
            model_name='trenink',
            name='prihlaseni_k_treninku',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trenink',
            name='misto',
            field=models.CharField(choices=[('venku', 'Venku'), ('mala_telocvicna', 'Malá tělovična'), ('velka_telocvicna', 'Velká tělocvična')], max_length=20, verbose_name='misto_konani_treninku'),
        ),
    ]
