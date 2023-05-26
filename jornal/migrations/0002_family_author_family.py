# Generated by Django 4.2.1 on 2023-05-23 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('brother_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='family',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='jornal.family'),
        ),
    ]
