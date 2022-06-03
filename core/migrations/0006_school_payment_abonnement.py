# Generated by Django 4.0.4 on 2022-05-30 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_abonnement'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Boy', 'Boy'), ('Girl', 'Girl')], default='Boy', max_length=10)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='abonnement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.abonnement'),
        ),
    ]
