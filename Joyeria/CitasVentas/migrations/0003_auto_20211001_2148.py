# Generated by Django 3.2.7 on 2021-10-02 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CitasVentas', '0002_auto_20211001_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordencompra',
            name='peso',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='piedraCentral',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='piedrasLaterales',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='producto',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='talla',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='tipoMaterial',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='agendamientocitas',
            name='telefono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='flujochats',
            name='chatNum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='numOrden',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='primerAbono',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordencompra',
            name='segundoAbono',
            field=models.IntegerField(),
        ),
    ]
