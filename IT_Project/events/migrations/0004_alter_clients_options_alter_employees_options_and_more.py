# Generated by Django 4.1.4 on 2022-12-21 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_events_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Клиенты', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='employees',
            options={'verbose_name': 'Работники', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Мероприятия', 'verbose_name_plural': 'Мероприятия'},
        ),
        migrations.AlterModelOptions(
            name='hotels',
            options={'verbose_name': 'Отели', 'verbose_name_plural': 'Отели'},
        ),
        migrations.AlterModelOptions(
            name='positions',
            options={'verbose_name': 'Должности', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name': 'Продажи', 'verbose_name_plural': 'Продажи'},
        ),
        migrations.AlterModelOptions(
            name='tours',
            options={'verbose_name': 'Туры', 'verbose_name_plural': 'Туры'},
        ),
        migrations.AlterModelOptions(
            name='typeoftour',
            options={'verbose_name': 'Виды туров', 'verbose_name_plural': 'Виды туров'},
        ),
        migrations.AlterField(
            model_name='clients',
            name='Telephone',
            field=models.CharField(max_length=16, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Positions', to='events.positions'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Clients', to='events.clients'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Employees', to='events.employees'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='Tours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Tours', to='events.tours'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='T_Events',
            field=models.ManyToManyField(related_name='Мероприятия', to='events.events'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='T_Hotels',
            field=models.ManyToManyField(related_name='Отели', to='events.hotels'),
        ),
        migrations.AlterField(
            model_name='typeoftour',
            name='Number_of_persons',
            field=models.IntegerField(null=True, verbose_name='Количество человек'),
        ),
    ]
