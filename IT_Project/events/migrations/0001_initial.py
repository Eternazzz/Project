
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=30, verbose_name='Должность')),
                ('Salary', models.IntegerField(verbose_name='Зарплата')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('Name', models.CharField(max_length=25, verbose_name='Имя')),
                ('Position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='events.positions')),
            ],
        ),
    ]
