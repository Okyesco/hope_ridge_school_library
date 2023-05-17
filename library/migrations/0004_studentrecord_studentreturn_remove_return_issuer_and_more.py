# Generated by Django 4.1.9 on 2023-05-17 10:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_record_date_borrowed_alter_return_return_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('stage', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('book_name', models.TextField(max_length=10000)),
                ('return_date', models.DateField()),
                ('date_borrowed', models.DateTimeField(default=datetime.datetime(2023, 5, 17, 10, 34, 26, 256462, tzinfo=datetime.timezone.utc))),
                ('comment', models.TextField(blank=True, max_length=10000)),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.issuer')),
            ],
        ),
        migrations.CreateModel(
            name='StudentReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('stage', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=10)),
                ('book_name', models.CharField(max_length=10000)),
                ('date_borrowed', models.DateTimeField()),
                ('return_date', models.DateTimeField(default=datetime.datetime(2023, 5, 17, 10, 34, 26, 257461, tzinfo=datetime.timezone.utc))),
                ('comment', models.TextField(blank=True, max_length=10000)),
                ('issuer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.issuer')),
            ],
        ),
        migrations.RemoveField(
            model_name='return',
            name='issuer',
        ),
        migrations.AlterField(
            model_name='teachersrecord',
            name='date_borrowed',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 17, 10, 34, 26, 261455, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='teachersreturn',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 17, 10, 34, 26, 260457, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.DeleteModel(
            name='Return',
        ),
    ]
