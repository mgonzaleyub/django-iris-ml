# Generated by Django 3.2.4 on 2021-07-08 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predict_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('sepal_length', models.DecimalField(decimal_places=2, max_digits=3)),
                ('sepal_width', models.DecimalField(decimal_places=2, max_digits=3)),
                ('petal_length', models.DecimalField(decimal_places=2, max_digits=3)),
                ('petal_width', models.DecimalField(decimal_places=2, max_digits=3)),
                ('prediction', models.CharField(choices=[('setosa', 'Setosa'), ('versicolor', 'Versicolor'), ('virginica', 'Virginica')], max_length=10)),
            ],
        ),
    ]
