# Generated by Django 3.0.2 on 2020-02-08 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('birth_year', models.SmallIntegerField()),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Кому одолжил(Имя)')),
                ('borrowed', models.DateField(null=True, verbose_name='Дата выдачи книги')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('year_release', models.SmallIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Friend')),
            ],
        ),
    ]
